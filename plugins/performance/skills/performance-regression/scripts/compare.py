"""Compare controlled samples. Signals are advisory, never release decisions."""
import argparse
import json
import math
import statistics
from pathlib import Path

ENV = ('os', 'arch', 'cpu', 'memory_bytes', 'node', 'browser', 'viewport', 'headless')
CONDITIONS = ('protocol', 'warmups', 'samples', 'cache', 'network', 'power')


def validate(report):
    if report.get('schema_version') != 1:
        raise ValueError('unsupported schema')
    for name in ('source_revision', 'toolkit_revision', 'scenario', 'captured_at'):
        if not isinstance(report.get(name), str) or not report[name].strip():
            raise ValueError('missing ' + name)
    if report.get('source_dirty') is not False:
        raise ValueError('source must be clean and pinned')
    for name, fields in [('environment', ENV), ('conditions', CONDITIONS)]:
        value = report.get(name, {})
        if any(k not in value or value[k] is None or value[k] == '' for k in fields):
            raise ValueError('incomplete ' + name)
    if not isinstance(report.get('fixture'), dict) or not report['fixture']:
        raise ValueError('missing fixture')
    if report['conditions']['power'] == 'unrecorded':
        raise ValueError('power conditions unrecorded')
    n = report['conditions']['samples']
    if type(n) is not int or n < 5:
        raise ValueError('at least five repeated samples required')
    if not isinstance(report.get('metrics'), dict) or not report['metrics']:
        raise ValueError('missing metrics')
    for metric in report['metrics'].values():
        if metric.get('unit') not in ('ms', 'bytes') or metric.get('direction') != 'lower':
            raise ValueError('unsupported metric')
        values = metric.get('samples', [])
        if len(values) != n or any(type(x) not in (int, float) or not math.isfinite(x) or x < 0 for x in values):
            raise ValueError('invalid or incomplete samples')


def summary(values):
    ordered = sorted(values)
    return {'n': len(values), 'median': statistics.median(values),
            'p95': ordered[math.ceil(.95 * len(values)) - 1],
            'min': ordered[0], 'max': ordered[-1],
            'stdev': statistics.pstdev(values)}


def compare(baseline, candidate):
    result = {'schema_version': 1, 'advisory': True, 'status': 'incomplete', 'metrics': {}}
    try:
        validate(candidate)
        if baseline is None:
            result['reason'] = 'baseline unavailable'
            return result
        validate(baseline)
    except (ValueError, TypeError, KeyError, AttributeError) as exc:
        result['reason'] = str(exc)
        return result
    for field in ('scenario', 'fixture', 'environment', 'conditions', 'toolkit_revision'):
        if baseline[field] != candidate[field]:
            result.update(status='incomparable', reason=field + ' changed')
            return result
    if baseline['metrics'].keys() != candidate['metrics'].keys():
        result['reason'] = 'metric coverage changed'
        return result
    for name, current in candidate['metrics'].items():
        prior = baseline['metrics'][name]
        if (prior['unit'], prior['direction']) != (current['unit'], current['direction']):
            result.update(status='incomparable', reason='metric definition changed: ' + name)
            return result
        b, c = summary(prior['samples']), summary(current['samples'])
        delta = c['median'] - b['median']
        # Complete sample separation is a conservative triage signal, not a
        # statistical significance test or a universal performance budget.
        signal = 'slower_sample_range' if c['min'] > b['max'] else 'overlapping_or_faster'
        result['metrics'][name] = {'unit': current['unit'], 'baseline': b, 'candidate': c,
                                  'median_delta': delta,
                                  'median_change_percent': 100 * delta / b['median'] if b['median'] else None,
                                  'signal': signal}
    result.update(status='comparable', baseline_revision=baseline['source_revision'],
                  candidate_revision=candidate['source_revision'],
                  experiments={'baseline': baseline.get('experiment'), 'candidate': candidate.get('experiment')})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path)
    parser.add_argument('--candidate', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    baseline = json.loads(args.baseline.read_text()) if args.baseline and args.baseline.exists() else None
    result = compare(baseline, json.loads(args.candidate.read_text()))
    with args.output.open('x') as out:
        json.dump(result, out, indent=2, allow_nan=False)
        out.write('\n')
    print(result['status'])
    # Regression signals remain advisory. Unusable evidence is a tooling error.
    return 0 if result['status'] == 'comparable' else 2


if __name__ == '__main__':
    raise SystemExit(main())
