"""Print exact UTC bounds for a week ending at local midnight; Python 3.9+."""
import argparse
from datetime import date, datetime, time, timedelta, timezone
import json
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def iso_utc(value):
    return value.astimezone(timezone.utc).isoformat().replace('+00:00', 'Z')


def bounds(end_date, timezone_name, first_start=None):
    if len(end_date) != 10 or date.fromisoformat(end_date).isoformat() != end_date:
        raise ValueError('end date must be YYYY-MM-DD')
    zone = ZoneInfo(timezone_name)
    cutoff = date.fromisoformat(end_date)
    local_start = datetime.combine(cutoff - timedelta(days=7), time.min, zone)
    local_end = datetime.combine(cutoff, time.min, zone)
    start = local_start.astimezone(timezone.utc)
    end = local_end.astimezone(timezone.utc)
    if first_start is not None:
        activated = datetime.fromisoformat(first_start.replace('Z', '+00:00'))
        if activated.tzinfo is None:
            raise ValueError('first start must include timezone')
        activated = activated.astimezone(timezone.utc)
        if not start <= activated < end:
            raise ValueError('first start must fall within this local week')
        start = activated
    return {'timezone': timezone_name, 'local_cutoff_date': end_date,
            'start': iso_utc(start), 'end': iso_utc(end),
            'elapsed_hours': round((end - start).total_seconds() / 3600, 6)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--timezone', required=True, help='IANA timezone, e.g. America/Los_Angeles')
    parser.add_argument('--end-date', required=True, help='local date at the end cutoff, YYYY-MM-DD')
    parser.add_argument('--first-start', help='recorded first activation timestamp with timezone')
    args = parser.parse_args()
    try:
        result = bounds(args.end_date, args.timezone, args.first_start)
    except (ValueError, ZoneInfoNotFoundError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
