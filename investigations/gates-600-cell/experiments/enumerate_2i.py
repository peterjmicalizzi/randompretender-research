"""Exact 2I word enumeration. Python 3.10+, standard library only.

No network, subprocesses, dependencies, or file writes. JSON goes to stdout.
Field elements are (a,b) meaning a+b*sqrt(5), with rational coefficients.
This is one implementation with internal checks, not independent verification.
"""
from fractions import Fraction as F
from itertools import permutations, product
from collections import deque, Counter
import json


def scalar(a=0, b=0):
    return (F(a), F(b))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def mul(x, y):
    return (x[0]*y[0] + 5*x[1]*y[1], x[0]*y[1] + x[1]*y[0])


def total(*xs):
    value = scalar()
    for x in xs:
        value = add(value, x)
    return value


def qmul(p, q):
    a,b,c,d = p
    e,f,g,h = q
    return (
        total(mul(a,e),neg(mul(b,f)),neg(mul(c,g)),neg(mul(d,h))),
        total(mul(a,f),mul(b,e),mul(c,h),neg(mul(d,g))),
        total(mul(a,g),neg(mul(b,h)),mul(c,e),mul(d,f)),
        total(mul(a,h),mul(b,g),neg(mul(c,f)),mul(d,e)),
    )


def conjugate(q):
    return (q[0], neg(q[1]), neg(q[2]), neg(q[3]))


def norm(q):
    return total(*(mul(x,x) for x in q))


def vertices():
    zero = scalar()
    points = set()
    for axis in range(4):
        for sign in (-1,1):
            q = [zero]*4
            q[axis] = scalar(sign)
            points.add(tuple(q))
    for signs in product((-1,1), repeat=4):
        points.add(tuple(scalar(F(s,2)) for s in signs))
    # Even permutations of (0, +/-1/2, +/-phi/2, +/-1/(2phi)).
    for signs in product((-1,1), repeat=3):
        raw = (zero, scalar(F(signs[0],2)),
               scalar(F(signs[1],4),F(signs[1],4)),
               scalar(F(-signs[2],4),F(signs[2],4)))
        for perm in permutations(range(4)):
            inversions = sum(perm[i] > perm[j] for i in range(4) for j in range(i+1,4))
            if inversions % 2 == 0:
                points.add(tuple(raw[i] for i in perm))
    return sorted(points)


def encode(q):
    return [[str(a),str(b)] for a,b in q]


def main():
    points = vertices()
    pointset = set(points)
    identity = (scalar(1),scalar(),scalar(),scalar())
    # a=(1+i+j+k)/2, b=(phi + j + (phi-1)k)/2. Append on the right.
    a = (scalar(F(1,2)),)*4
    b = (scalar(F(1,4),F(1,4)),scalar(),scalar(F(1,2)),scalar(F(-1,4),F(1,4)))
    generators = {'a':a,'A':conjugate(a),'b':b,'B':conjugate(b)}
    assert len(points) == 120
    assert all(norm(q) == scalar(1) for q in points)
    assert all(g in pointset for g in generators.values())
    assert all(conjugate(q) in pointset and qmul(q,conjugate(q)) == identity for q in points)
    assert all(qmul(p,q) in pointset for p in points for q in points)
    words = {identity:''}
    queue = deque([identity])
    while queue:
        q = queue.popleft()
        for letter,g in generators.items():
            target = qmul(q,g)
            if target not in words:
                words[target] = words[q] + letter
                queue.append(target)
    assert len(words) == 120, 'Chosen generators did not reach all of 2I'
    for q,word in words.items():
        actual = identity
        for letter in word:
            actual = qmul(actual,generators[letter])
        assert actual == q
    histogram = Counter(map(len,words.values()))
    out = {
        'schema_version':1,
        'experiment_id':'rp:experiment:2i-words:001',
        'object_id':'rp:object:2i-coordinate-presentation:001',
        'field':'Q(sqrt(5)); each coordinate is [a,b] for a+b*sqrt(5)',
        'coordinate_order':'real,i,j,k',
        'multiplication':'Hamilton; ij=k; append generator on the right',
        'phase_convention':'SU(2); q and -q are distinct',
        'cost':'one per letter; alphabet a,A,b,B, capitals are inverses',
        'vertex_count':len(points),
        'ordered_products_checked':len(points)**2,
        'vertices_reached':len(words),
        'max_shortest_word_length':max(histogram),
        'shortest_word_length_histogram':dict(sorted(histogram.items())),
        'generators':{letter:encode(g) for letter,g in generators.items()},
        'collision':{'word_1':'aA','word_2':'','endpoint':encode(identity)},
        'vertices':[{'local_index':i,'coordinates':encode(q),'shortest_word':words[q]} for i,q in enumerate(points)],
        'checks':['120 distinct vertices','exact norm one','exact inverse membership and product',
                  'all 14400 ordered products remain in vertex set','all vertices reached',
                  'every recorded word replays to its endpoint'],
    }
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
