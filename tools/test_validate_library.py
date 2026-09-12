"""Tests for the library validator. Read-only, like the validator: nothing here executes
experiment code. Each test copies the library to a temporary directory, alters one thing,
and checks that the validator refuses it with a message naming the problem.

    python tools/test_validate_library.py
"""
from pathlib import Path
import json
import shutil
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_library import validate  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
REPRO = Path('investigations/gates-600-cell/reproductions/001/run.json')

passed = failed = 0


def copy_library(dst):
    shutil.copytree(ROOT, dst, ignore=shutil.ignore_patterns('.git', '__pycache__'), dirs_exist_ok=True)


def edit_json(path, change):
    data = json.loads(path.read_text(encoding='utf-8'))
    change(data)
    path.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')


def expect_pass(name):
    global passed, failed
    with tempfile.TemporaryDirectory() as tmp:
        copy_library(tmp)
        try:
            validate(Path(tmp))
            passed += 1; print(f'  ok   {name}')
        except (ValueError, KeyError, TypeError, OSError) as error:
            failed += 1; print(f'  FAIL {name}: unexpectedly rejected: {error}')


def expect_reject(name, path, change, fragment):
    global passed, failed
    with tempfile.TemporaryDirectory() as tmp:
        copy_library(tmp)
        edit_json(Path(tmp) / path, change)
        try:
            validate(Path(tmp))
            failed += 1; print(f'  FAIL {name}: accepted')
        except (ValueError, KeyError, TypeError, OSError) as error:
            if fragment in str(error):
                passed += 1; print(f'  ok   {name}')
            else:
                failed += 1; print(f'  FAIL {name}: rejected for the wrong reason: {error}')


print('-- the library as committed')
expect_pass('the committed library validates')

print('-- a reproduction must be bound to the execution it reproduces')
expect_reject('an altered comparison hash is rejected', REPRO,
              lambda d: d['compared_against'].__setitem__('sha256', '0' * 64), 'comparison artifact')
expect_reject('a comparison path that is not an artifact of the reproduced execution is rejected', REPRO,
              lambda d: d['compared_against'].__setitem__('path', '../../experiments/run.json'), 'comparison artifact')
expect_reject('a reproduction of a different object than the execution it names is rejected', REPRO,
              lambda d: d.__setitem__('object_id', 'rp:object:something-else:001'), 'object')
expect_reject('a reproduction naming an unlisted execution is rejected', REPRO,
              lambda d: d.__setitem__('reproduces', 'rp:execution:does-not-exist:001'), 'listed execution')
expect_reject('a reproduction without stated shared dependencies is rejected', REPRO,
              lambda d: d.__setitem__('shared_dependencies', []), 'shared dependencies')
expect_reject('a reproduction without a stated comparison is rejected', REPRO,
              lambda d: d.__setitem__('comparison', ''), 'what was compared')

print('-- an execution record still has to match its files')
expect_reject('an altered artifact hash is rejected', REPRO,
              lambda d: d['artifacts'][0].__setitem__('sha256', '0' * 64), 'checksum')

print('-- a claim cannot list a reproduction that is not one')
expect_reject('a claim listing the starter run as a reproduction is rejected',
              Path('investigations/gates-600-cell/claims/001-generator-reachability.json'),
              lambda d: d.__setitem__('independent_reproductions', ['../experiments/run.json']), 'not a reproduction record')
expect_reject('a claim with a hand-assigned status is rejected',
              Path('investigations/gates-600-cell/claims/001-generator-reachability.json'),
              lambda d: d.__setitem__('status', 'supported'), 'truth status')

print(f'\n{passed} passed, {failed} failed')
sys.exit(1 if failed else 0)
