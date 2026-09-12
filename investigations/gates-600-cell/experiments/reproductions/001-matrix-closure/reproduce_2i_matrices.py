"""Independent reproduction of rp:execution:2i-words:001 by a different construction.

SPDX-License-Identifier: Apache-2.0

Written from BRIEF.md and the recorded result.json only. The starter's helper functions
were not used as a reference for the group operation. What makes this a separate
implementation rather than a replay:

  * The group is built as the CLOSURE of the two generators under matrix multiplication,
    not from an explicit list of 120 coordinates. If the closure has 120 elements and
    equals the recorded coordinate set under the brief's matrix map, the two
    constructions agree.
  * The group operation is 2x2 complex matrix multiplication over Q(sqrt5)(i), using the
    brief's stated correspondence  a+bi+cj+dk -> [[a+bi, c+di], [-c+di, a-bi]].
  * The brief asks for that correspondence to be verified explicitly. It is checked here
    for all 14,400 ordered pairs against a Hamilton product written from the textbook
    formula.
  * Shortest words come from a breadth-first search over right multiplication. The
    per-vertex distances and the histogram are compared with the record, and every
    recorded shortest word is replayed in matrices to its recorded endpoint.

Python 3.10+, standard library only. No network, no subprocesses, no file writes; the
report is JSON on stdout. Exit status 0 when every check passes, 1 otherwise.

    python investigations/gates-600-cell/experiments/reproductions/001-matrix-closure/reproduce_2i_matrices.py

An optional argument names a different result.json to compare against.
"""
from fractions import Fraction as Fr
from collections import deque, Counter
from pathlib import Path
import json, sys, time, hashlib

# ----------------------------------------------------------------- Q(sqrt5): (r, s) = r + s*sqrt5
def f_add(x, y): return (x[0] + y[0], x[1] + y[1])
def f_sub(x, y): return (x[0] - y[0], x[1] - y[1])
def f_mul(x, y): return (x[0]*y[0] + 5*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def f_neg(x):    return (-x[0], -x[1])
F0 = (Fr(0), Fr(0)); F1 = (Fr(1), Fr(0))
def f(r, s=0):   return (Fr(r), Fr(s))

# ----------------------------------------------------------------- Q(sqrt5)(i): (re, im), each in Q(sqrt5)
def c_add(x, y): return (f_add(x[0], y[0]), f_add(x[1], y[1]))
def c_mul(x, y): return (f_sub(f_mul(x[0], y[0]), f_mul(x[1], y[1])), f_add(f_mul(x[0], y[1]), f_mul(x[1], y[0])))
def c_neg(x):    return (f_neg(x[0]), f_neg(x[1]))
def c_conj(x):   return (x[0], f_neg(x[1]))
C0 = (F0, F0); C1 = (F1, F0)

# ----------------------------------------------------------------- 2x2 matrices as tuples (m00, m01, m10, m11)
def m_mul(P, Q):
    return (c_add(c_mul(P[0], Q[0]), c_mul(P[1], Q[2])),
            c_add(c_mul(P[0], Q[1]), c_mul(P[1], Q[3])),
            c_add(c_mul(P[2], Q[0]), c_mul(P[3], Q[2])),
            c_add(c_mul(P[2], Q[1]), c_mul(P[3], Q[3])))
def m_dagger(P):   # conjugate transpose; for SU(2) this is the inverse
    return (c_conj(P[0]), c_conj(P[2]), c_conj(P[1]), c_conj(P[3]))
def m_det(P):
    return c_add(c_mul(P[0], P[3]), c_neg(c_mul(P[1], P[2])))
IDENT = (C1, C0, C0, C1)

# The brief's stated correspondence.
def quat_to_matrix(q):
    a, b, c, d = q
    return ((a, b), (c, d), (f_neg(c), d), (a, f_neg(b)))
def matrix_to_quat(M):
    (a, b), (c, d) = M[0], M[1]
    return (a, b, c, d)

# Textbook Hamilton product, written independently for the correspondence check.
def hamilton(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return (f_sub(f_sub(f_sub(f_mul(a1,a2), f_mul(b1,b2)), f_mul(c1,c2)), f_mul(d1,d2)),
            f_sub(f_add(f_add(f_mul(a1,b2), f_mul(b1,a2)), f_mul(c1,d2)), f_mul(d1,c2)),
            f_add(f_add(f_sub(f_mul(a1,c2), f_mul(b1,d2)), f_mul(c1,a2)), f_mul(d1,b2)),
            f_add(f_sub(f_add(f_mul(a1,d2), f_mul(b1,c2)), f_mul(c1,b2)), f_mul(d1,a2)))

def parse_field(pair):   # result.json encodes each coordinate as ["r", "s"] meaning r + s*sqrt5
    return (Fr(pair[0]), Fr(pair[1]))

def main(result_path):
    t0 = time.perf_counter()
    rec = json.loads(Path(result_path).read_text(encoding='utf-8'))
    report = {'schema_version': 1, 'id': 'rp:reproduction-report:2i-words-matrix-closure:001',
              'reproduces': 'rp:execution:2i-words:001', 'method': 'closure of <a,b> under 2x2 matrix multiplication over Q(sqrt5)(i)',
              'checks': []}
    def check(name, ok, detail=''):
        report['checks'].append({'check': name, 'passed': bool(ok), **({'detail': detail} if detail else {})})
        if not ok: report['reproduced'] = False

    # Generators from the brief, not from the record: a=(1+i+j+k)/2, b=(phi + j + (phi-1)k)/2, phi=(1+sqrt5)/2.
    half = f(Fr(1,2)); phi_half = f(Fr(1,4), Fr(1,4)); phim1_half = f(Fr(-1,4), Fr(1,4))
    a_q = (half, half, half, half)
    b_q = (phi_half, F0, half, phim1_half)
    a, b = quat_to_matrix(a_q), quat_to_matrix(b_q)
    gens = {'a': a, 'A': m_dagger(a), 'b': b, 'B': m_dagger(b)}
    check('generators are special unitary (det 1, dagger is inverse)',
          all(m_det(g) == C1 and m_mul(g, m_dagger(g)) == IDENT for g in gens.values()))
    check('generators match the record', all(quat_to_matrix(tuple(parse_field(x) for x in rec['generators'][k])) == gens[k] for k in gens))

    # Closure of <a, b> under multiplication.
    group = {IDENT}; frontier = [IDENT]
    while frontier:
        nxt = []
        for g in frontier:
            for h in (a, b):
                p = m_mul(g, h)
                if p not in group: group.add(p); nxt.append(p)
        frontier = nxt
        if len(group) > 200: break
    check('closure of <a,b> has exactly 120 elements', len(group) == 120, f'{len(group)}')
    check('closure is closed under inverse', all(m_dagger(g) in group for g in group))
    check('all 14400 ordered products stay in the closure', all(m_mul(p, q) in group for p in group for q in group))
    check('every element has det 1', all(m_det(g) == C1 for g in group))

    # Same set as the recorded coordinates, under the brief's map.
    recorded = {quat_to_matrix(tuple(parse_field(x) for x in v['coordinates'])) for v in rec['vertices']}
    check('record lists 120 distinct coordinates', len(recorded) == 120 and len(rec['vertices']) == 120)
    check('closure equals the recorded coordinate set', recorded == group)
    check('the record keeps q and -q distinct (SU(2), not the projective quotient)',
          all(m_mul(g, quat_to_matrix((f(-1), F0, F0, F0))) in group for g in group) and len(group) == 120)

    # The correspondence the brief asks to be verified: M(p)M(q) == M(pq) for every ordered pair.
    quats = [matrix_to_quat(g) for g in group]
    check('matrix product agrees with the Hamilton product on all 14400 ordered pairs (map is a homomorphism)',
          all(m_mul(quat_to_matrix(p), quat_to_matrix(q)) == quat_to_matrix(hamilton(p, q)) for p in quats for q in quats))

    # Shortest words: BFS over right multiplication by the four letters.
    dist = {IDENT: 0}; queue = deque([IDENT])
    while queue:
        g = queue.popleft()
        for L, h in gens.items():
            p = m_mul(g, h)
            if p not in dist: dist[p] = dist[g] + 1; queue.append(p)
    check('all 120 elements are reached by the alphabet a,A,b,B', len(dist) == 120)
    hist = dict(sorted(Counter(dist.values()).items()))
    rec_hist = {int(k): v for k, v in rec['shortest_word_length_histogram'].items()}
    check('shortest-word-length histogram matches the record', hist == rec_hist, f'mine {hist} record {rec_hist}')
    check('maximum shortest word length matches', max(hist) == rec['max_shortest_word_length'], f'{max(hist)} vs {rec["max_shortest_word_length"]}')

    # Replay every recorded shortest word in matrices; it must land on its recorded endpoint and be minimal.
    ok_replay = True; ok_len = True
    for v in rec['vertices']:
        M = quat_to_matrix(tuple(parse_field(x) for x in v['coordinates']))
        cur = IDENT
        for L in v['shortest_word']: cur = m_mul(cur, gens[L])
        if cur != M: ok_replay = False
        if dist[M] != len(v['shortest_word']): ok_len = False
    check('every recorded word replays to its recorded endpoint (right multiplication, written order)', ok_replay)
    check('every recorded word has the minimal length for its endpoint', ok_len)
    check('the recorded collision aA = identity holds', m_mul(gens['a'], gens['A']) == IDENT)

    report.setdefault('reproduced', True)
    report['histogram'] = {str(k): v for k, v in hist.items()}
    report['runtime_seconds'] = round(time.perf_counter() - t0, 3)
    report['python'] = sys.version.split()[0]
    report['compared_result_sha256'] = hashlib.sha256(Path(result_path).read_bytes()).hexdigest()
    report['shared_assumptions'] = [
        'Q(sqrt5) arithmetic on Fraction pairs is exact; both implementations rely on that.',
        "The brief's matrix correspondence is taken as the definition of the matrix side; it is then checked to be a homomorphism.",
        'Generators, conventions and coordinate encoding are read from the brief and the record, so an error in those definitions would be shared.',
        'Both implementations were produced by AI assistants under the direction of the same person; the implementations and models are independent, the direction is not.',
    ]
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report['reproduced'] else 1

if __name__ == '__main__':
    default = Path(__file__).resolve().parents[2] / 'result.json'
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else default))
