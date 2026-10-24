"""Offline decision report from minimized source exports; Python 3.9+, stdlib only."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re

REVISION = 'reporting/0.1.0'
SOURCES = ('tally', 'gmail', 'analytics')
METRICS = ('visits', 'page_views', 'lcp_p75_ms', 'inp_p75_ms', 'cls_p75')


def time(value):
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('timestamps must include timezone')
    return parsed.astimezone(timezone.utc)


def label(value):
    if not isinstance(value, str) or not re.fullmatch(r'[a-z][a-z0-9_-]{0,47}', value):
        raise ValueError('configuration labels must be short lowercase slugs')
    return value


def ready(source, start, end, now, max_age):
    if not isinstance(source, dict) or source.get('status') != 'ok':
        return 'unavailable'
    try:
        fetched = time(source['fetched_at'])
        coverage = source['coverage']
        if fetched > now or (now-fetched).total_seconds() > max_age * 3600:
            return 'stale'
        if time(coverage['start']) > start or time(coverage['end']) < end:
            return 'partial'
    except (KeyError, TypeError, ValueError, AttributeError):
        return 'invalid'
    return 'ok'


def feedback_adapter(source, allowed):
    records = source['records']
    if not isinstance(records, list):
        raise ValueError('records must be a list')
    clean = []
    identities = {}
    for record in records:
        # IDs remain internal; neither identifiers nor arbitrary source text enters output.
        rid = record['id']
        if not isinstance(rid, str) or not rid:
            raise ValueError('record requires id')
        created = time(record['created_at'])
        status = record.get('status', 'unknown')
        if status not in ('open', 'resolved', 'unknown'):
            raise ValueError('invalid triage status')
        qa = record.get('is_qa', False)
        if not isinstance(qa, bool):
            raise ValueError('is_qa must be boolean')
        fields = {k: record.get(k) if record.get(k) in allowed[k] else 'unclassified'
                  for k in ('product', 'contact_type', 'theme')}
        submission = record.get('submission_id')
        if submission is not None and (not isinstance(submission, str) or not submission):
            raise ValueError('invalid submission reference')
        normalized = dict(fields, id=rid, created=created, status=status, is_qa=qa,
                          submission_id=submission)
        if rid in identities and identities[rid] != normalized:
            raise ValueError("conflicting duplicate record")
        identities[rid] = normalized
        clean.append(normalized)
    return clean


def tally_adapter(source, allowed):
    return feedback_adapter(source, allowed)


def gmail_adapter(source, allowed):
    return feedback_adapter(source, allowed)


def analytics_adapter(source):
    values = source['metrics']
    result = {}
    for name in METRICS:
        value = values.get(name)
        if value is not None and (type(value) not in (int, float) or value < 0 or value != value or value == float('inf')):
            raise ValueError('invalid analytics value')
        result[name] = value
    return result


def generate(data):
    start, end, now = time(data['window']['start']), time(data['window']['end']), time(data['as_of'])
    if not start < end <= now:
        raise ValueError('window must be nonempty and end no later than as_of')
    config = data['config']
    allowed = {key: {label(v) for v in config[name]} for key, name in
               (('product', 'products'), ('contact_type', 'contact_types'), ('theme', 'themes'))}
    max_age = config.get('max_source_age_hours', 48)
    if type(max_age) not in (float, int) or not 0 < max_age <= 8760:
        raise ValueError('invalid maximum source age')
    report = dict(schema_version=1, skill_revision=REVISION, window={'start': start.isoformat(), 'end': end.isoformat()},
                  as_of=now.isoformat(), sources={}, feedback={}, analytics=None,
                  findings=[], decisions_needed=[], limitations=[
                      'Counts describe records and visits, not unique customers or demand.',
                      'QA exclusion requires source tagging; deployment/test traffic may remain in analytics.',
                      'Themes are approved categories assigned upstream; message text is not retained.',
                      'Unresolved age covers supplied open records only; completeness of backlog is not inferred.'])
    loaded = {}
    for name in SOURCES:
        source = data.get('sources', {}).get(name, {})
        state = ready(source, start, end, now, max_age)
        report['sources'][name] = {'status': state, 'fetched_at': None, 'coverage': None, 'input_records': None}
        if state != 'ok':
            continue
        try:
            if name == 'analytics':
                report['analytics'] = analytics_adapter(source)
            else:
                loaded[name] = (tally_adapter if name == 'tally' else gmail_adapter)(source, allowed)
                report['sources'][name]['input_records'] = len(loaded[name])
            report['sources'][name]['fetched_at'] = time(source['fetched_at']).isoformat()
            report['sources'][name]['coverage'] = {key: time(source['coverage'][key]).isoformat() for key in ('start', 'end')}
        except (KeyError, TypeError, ValueError, AttributeError):
            report['sources'][name]['status'] = 'invalid'
    seen, tally_ids = set(), {r['id'] for r in loaded.get('tally', [])}
    included = []
    ages = []
    exclusions = Counter()
    for name in ('tally', 'gmail'):
        for r in loaded.get(name, []):
            key = (name, r['id'])
            if key in seen:
                exclusions['duplicate_records'] += 1
                continue
            seen.add(key)
            # Linked notifications are never counted as new feedback, even if Tally import fails.
            if name == 'gmail' and r['submission_id']:
                exclusions['linked_notifications'] += 1
                if r['submission_id'] not in tally_ids:
                    exclusions['unmatched_notifications'] += 1
                continue
            if r['is_qa']:
                exclusions['qa_records'] += 1
                continue
            if r['created'] >= end:
                exclusions['outside_window'] += 1
                continue
            if r['status'] == 'open':
                ages.append(round((end-r['created']).total_seconds()/86400, 2))
            if r['created'] < start:
                exclusions['outside_window'] += 1
                continue
            included.append(r)
    complete = all(report['sources'][k]['status'] == 'ok' for k in ('tally', 'gmail'))
    report['feedback'] = {'complete': complete, 'total': len(included) if complete else None,
        'observed_records': len(included) if loaded else None,
        'by_product': dict(sorted(Counter(r['product'] for r in included).items())) if loaded else None,
        'by_contact_type': dict(sorted(Counter(r['contact_type'] for r in included).items())) if loaded else None,
        'themes': dict(sorted(Counter(r['theme'] for r in included).items())) if loaded else None,
        'open_records_in_supplied_backlog': len(ages) if loaded else None,
        'oldest_open_days': max(ages) if ages else None, 'exclusions': dict(exclusions)}
    for name, info in report['sources'].items():
        if info['status'] != 'ok':
            report['decisions_needed'].append({'code': 'restore_source', 'source': name})
    for theme, count in (report['feedback']['themes'] or {}).items():
        if theme != 'unclassified' and count >= 2:
            report['findings'].append({'code': 'repeated_theme', 'theme': theme, 'records': count,
                                       'suggested_action': 'Review source cases before prioritizing a change.'})
    if ages and max(ages) >= 7:
        report['findings'].append({'code': 'aging_open_case', 'days': max(ages),
                                  'suggested_action': 'Review the oldest open case in its source system.'})
    report['status'] = 'complete' if all(v['status'] == 'ok' for v in report['sources'].values()) else 'incomplete'
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    try:
        report = generate(json.loads(args.input.read_text()))
        # Exclusive create prevents accidental destruction; caller owns private destination/retention.
        import os
        fd = os.open(args.output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, 'w') as out:
            json.dump(report, out, indent=2, allow_nan=False)
            out.write('\n')
    except (ValueError, KeyError, TypeError, OSError, AttributeError):
        raise SystemExit('REPORT FAILED: invalid input or unavailable output; no source values logged')
    print('REPORT ' + report['status'].upper())


if __name__ == '__main__':
    main()
