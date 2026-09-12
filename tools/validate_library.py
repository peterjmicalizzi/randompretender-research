"""Read-only consistency checks. Never imports or executes experiment code.

Review this validator itself before running a contributed revision. Hash equality is
artifact integrity, not mathematical verification or proof of authorship.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def safe_file(root, base, reference):
    require(isinstance(reference,str) and reference, 'Missing file reference')
    path = (base / reference).resolve()
    require(path.is_relative_to(root), f'Path leaves library: {reference}')
    require(path.is_file(), f'Missing artifact: {reference}')
    require(path.stat().st_size <= 2_000_000, f'Artifact exceeds initial size policy: {reference}')
    return path


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def validate(root=ROOT):
    root = root.resolve()
    require(not (root/'.github/workflows').exists(), 'Automatic workflows are outside this library boundary')
    for path in root.rglob('*'):
        if '.git' in path.relative_to(root).parts:
            continue
        require(not path.is_symlink(), f'Symlink not allowed: {path.name}')
        if path.is_file():
            require(path.stat().st_size <= 2_000_000, f'File too large: {path.name}')
    manifests = list((root/'investigations').glob('*/workspace.json'))
    require(manifests, 'No investigation manifest')
    ids = set()
    for path in manifests:
        workspace = read_json(path)
        require(workspace.get('schema_version') == 1, 'Unknown workspace schema')
        require(workspace['id'] not in ids, 'Duplicate workspace ID')
        ids.add(workspace['id'])
        safe_file(root,path.parent,workspace['brief'])
        known_runs = {}
        known_ids = {}
        for ref in workspace['experiment_records']:
            record_path = safe_file(root,path.parent,ref)
            record = read_json(record_path)
            require(record.get('schema_version') == 1, 'Unknown execution schema')
            require(record['id'] not in ids, 'Duplicate execution ID')
            ids.add(record['id'])
            kind = record.get('execution_kind')
            require(kind in ('local-single-implementation', 'independent-reproduction'), f'Unexpected evidence kind: {kind}')
            if kind == 'independent-reproduction':
                # A reproduction names the execution it reproduces, which must be listed earlier
                # in the workspace, and states what the two runs share. Neither field is a
                # verdict: the validator checks that the record is complete, not that it is right.
                require(record.get('reproduces') in known_ids, 'Reproduction does not name a listed execution')
                original = known_ids[record['reproduces']]
                require(record.get('object_id') == original.get('object_id'), 'Reproduction object differs from the reproduced execution')
                compared = record.get('compared_against') or {}
                compared_file = safe_file(root, record_path.parent, compared.get('path'))
                original_hashes = {a['sha256'] for a in original['artifacts']}
                require(compared.get('sha256') in original_hashes, 'Reproduction comparison artifact is not a recorded artifact of the reproduced execution')
                require(hashlib.sha256(compared_file.read_bytes()).hexdigest() == compared['sha256'], 'Reproduction comparison artifact checksum mismatch')
                require(record.get('shared_dependencies'), 'Reproduction must state shared dependencies')
                require(record.get('comparison'), 'Reproduction must state what was compared')
            for artifact in record['artifacts']:
                file = safe_file(root,record_path.parent,artifact['path'])
                actual = hashlib.sha256(file.read_bytes()).hexdigest()
                require(actual == artifact['sha256'], f'Artifact checksum mismatch: {file.name}')
            require(record.get('runtime') and record.get('recorded_at_utc'), 'Missing execution context')
            known_runs[record_path] = record
            known_ids[record['id']] = record
        for ref in workspace['claim_files']:
            claim_path = safe_file(root,path.parent,ref)
            claim = read_json(claim_path)
            require(claim.get('schema_version') == 1, 'Unknown claim schema')
            require(claim['id'] not in ids, 'Duplicate claim ID')
            ids.add(claim['id'])
            require(claim.get('statement') and claim.get('assumptions'), 'Claim missing statement or assumptions')
            require('status' not in claim, 'Do not assign a truth status by hand')
            for evidence in claim['evidence_records']:
                run_path = safe_file(root,claim_path.parent,evidence)
                require(run_path in known_runs, 'Evidence not listed by workspace')
                require(known_runs[run_path]['object_id'] == claim['object_id'], 'Claim/evidence object mismatch')
            for field in ('independent_reproductions','scoped_reviews','formal_proofs','challenges'):
                require(isinstance(claim.get(field),list), f'Missing evidence list: {field}')
            for ref in claim['independent_reproductions']:
                run_path = safe_file(root,claim_path.parent,ref)
                require(run_path in known_runs, 'Reproduction not listed by workspace')
                require(known_runs[run_path].get('execution_kind') == 'independent-reproduction', 'Listed reproduction is not a reproduction record')
                require(known_runs[run_path]['object_id'] == claim['object_id'], 'Claim/reproduction object mismatch')
    return len(manifests), len(ids)


if __name__ == '__main__':
    try:
        workspaces, records = validate()
    except (ValueError,KeyError,TypeError,OSError) as error:
        raise SystemExit(f'FAIL: {error}')
    print(f'PASS: {workspaces} workspace(s), {records} record IDs; references and artifact hashes agree.')
    print('This is a consistency check, not an independent computation or mathematical certificate.')
