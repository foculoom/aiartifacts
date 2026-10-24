#!/usr/bin/env python3
"""Compile a local Keychain launcher for ONE reviewed profile. No secrets read."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


def validate_tasks(cfg):
    """Reject unpinned interpreter inputs before compiling the trusted policy."""
    for task in cfg['tasks'].values():
        argv, files, cwd = task['argv'], task['reviewed_files'], Path(task['cwd'])
        if not argv or not Path(argv[0]).is_absolute() or argv[0] not in files:
            raise ValueError('Task executable must be absolute and pinned.')
        if not cwd.is_absolute():
            raise ValueError('Task directory must be absolute.')
        if Path(argv[0]).name.startswith('python'):
            if len(argv) < 3 or argv[1] != '-I' or not Path(argv[2]).is_absolute() or argv[2] not in files:
                raise ValueError('Python tasks require -I and an absolute pinned script; no -c or -m.')
        for arg in argv[1:]:
            path = Path(arg)
            if not path.is_absolute() and (cwd / path).is_file():
                raise ValueError('Relative task files are forbidden; resolve and pin them.')
            if path.is_absolute() and path.is_file() and arg not in files:
                raise ValueError('Task file arguments must be pinned.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', required=True)
    parser.add_argument('--python', required=True)
    args = parser.parse_args()
    os.umask(0o077)
    profile = Path(args.profile).resolve()
    cfg = json.loads(profile.read_text())
    validate_tasks(cfg)
    runner = Path(__file__).with_name('runner.py').resolve()
    python = Path(args.python).resolve()
    output = Path(cfg['keychain_helper'])
    if output.exists() or output.is_symlink():
        raise SystemExit('Refusing to replace a Keychain-trusted binary; review a new version explicitly.')
    if not output.is_absolute() or output.parent != profile.parent:
        raise SystemExit('Launcher must be beside the private profile.')
    pins = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in (profile, runner, python)}
    # JSON string encoding is valid Swift for these reviewed paths; reject Swift
    # interpolation syntax rather than allowing generated source execution.
    strings = [str(profile), str(runner), str(python), cfg['keychain_service'], cfg['keychain_account'], *cfg['tasks']]
    if any('\\' in value or '\n' in value for value in strings):
        raise SystemExit('Unsupported path or identifier encoding.')
    quote = json.dumps
    source = 'import Foundation\nenum LaunchConfig {\n'
    for key, value in [('service', cfg['keychain_service']), ('account', cfg['keychain_account']),
                       ('profile', str(profile)), ('runner', str(runner)), ('python', str(python))]:
        source += f' static let {key} = {quote(value)}\n'
    source += ' static let tasks = ' + quote(list(cfg['tasks'])) + '\n'
    source += ' static let files = [' + ','.join(quote(k) + ':' + quote(v) for k, v in pins.items()) + ']\n}\n'
    generated = profile.parent / 'LaunchConfig.swift'
    generated.write_text(source)
    main_source = profile.parent / 'main.swift'
    main_source.write_bytes(Path(__file__).with_name('keychain.swift').read_bytes())
    result = subprocess.run(['/usr/bin/xcrun', 'swiftc', '-module-cache-path', str(profile.parent / 'module-cache'),
                             str(main_source), str(generated), '-o', str(output)], capture_output=True)
    if result.returncode:
        raise SystemExit('Swift compilation failed; no credential has been read.')
    output.chmod(0o700)
    print(json.dumps({'status': 'compiled', 'launcher_sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
                      'pinned_files': pins, 'tasks': list(cfg['tasks'])}, sort_keys=True))


if __name__ == '__main__':
    main()
