"""Offline manifest or anonymous HTTPS readback. No credentials or deployment."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
from urllib.error import HTTPError
from urllib.parse import urlsplit, quote
from urllib.request import Request, build_opener, HTTPRedirectHandler

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def digest(data):
    return hashlib.sha256(data).hexdigest()

def parse_manifest(value):
    """Reject duplicate members before JSON can silently discard inventory."""
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('Duplicate manifest member')
            result[key] = value
        return result
    return json.loads(value, object_pairs_hook=unique_object)

def manifest(root):
    root = Path(root)
    if root.is_symlink() or not root.is_dir():
        raise ValueError('Regular payload directory required')
    files = {}
    for p in sorted(root.rglob('*')):
        if p.is_symlink():
            raise ValueError('Symlink in payload')
        if p.is_file():
            files[p.relative_to(root).as_posix()] = digest(p.read_bytes())
    if not files:
        raise ValueError('Empty payload')
    return {'version': 1, 'files': files}

def checked_files(record):
    """Validate the complete inventory before constructing a network client."""
    if (not isinstance(record, dict) or type(record.get('version')) is not int or
            record['version'] != 1 or not isinstance(record.get('files'), dict) or not record['files']):
        raise ValueError('Invalid manifest')
    for name, expected in record['files'].items():
        if not isinstance(name, str):
            raise ValueError('Unsafe manifest path')
        p = PurePosixPath(name)
        if (p.is_absolute() or any(part in ('', '.', '..') for part in name.split('/')) or
                str(p) != name or '\\' in name):
            raise ValueError('Unsafe manifest path')
        if not isinstance(expected, str) or len(expected) != 64 or any(c not in '0123456789abcdef' for c in expected):
            raise ValueError('Invalid digest')
    return record['files']

def verify(record, origin):
    url = urlsplit(origin)
    if url.scheme != 'https' or not url.hostname or url.username or url.password or url.path not in ('', '/') or url.query or url.fragment:
        raise ValueError('Plain HTTPS origin required')
    files = checked_files(record)
    opener = build_opener(NoRedirect())
    results = []
    for name, expected in files.items():
        route = name[:-10] if (name == 'index.html' or name.endswith('/index.html')) else name
        status = None
        try:
            request = Request(origin.rstrip('/') + '/' + quote(route), headers={'Accept-Encoding': 'identity', 'User-Agent': 'curl/8.7.1'})
            with opener.open(request, timeout=30) as response:
                status = response.status
                data = response.read(16*1024*1024+1)
                result = 'exact' if response.status == 200 and len(data) <= 16*1024*1024 and digest(data) == expected else 'mismatch'
        except HTTPError as error:
            status = error.code
            result = 'unavailable'
        except Exception:
            result = 'unavailable'
        results.append({'path': name, 'result': result, 'http_status': status})
    return {'status': 'passed' if all(x['result']=='exact' for x in results) else 'incomplete', 'origin': origin, 'files': results}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--root',type=Path)
    group.add_argument('--manifest',type=Path)
    parser.add_argument('--origin')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():
        parser.error('Output already exists')
    if args.root and args.output.resolve().is_relative_to(args.root.resolve()):
        parser.error('Evidence must stay outside the payload')
    if args.manifest and not args.origin:
        parser.error('--origin required for readback')
    result=manifest(args.root) if args.root else verify(parse_manifest(args.manifest.read_text()),args.origin)
    with args.output.open('x') as f:
        json.dump(result,f,indent=2);f.write('\n')
    print('PASS' if result.get('status','passed')=='passed' else 'CHECK INCOMPLETE')
    return 0 if result.get('status','passed')=='passed' else 1

if __name__=='__main__':
    raise SystemExit(main())
