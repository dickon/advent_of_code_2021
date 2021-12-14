import pprint
from  collections import Counter
sample="""
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

real = """PFVKOBSHPSPOOOCOOHBP

FV -> C
CP -> K
FS -> K
VF -> N
HN -> F
FF -> N
SS -> K
VS -> V
BV -> F
HC -> K
BP -> F
OV -> N
BF -> V
VH -> V
PF -> N
FC -> S
CS -> B
FK -> N
VK -> H
FN -> P
SH -> V
CV -> K
HP -> K
HO -> C
NO -> V
CK -> C
VB -> S
OC -> N
NS -> C
NF -> H
SF -> N
NK -> S
NP -> P
OO -> S
NH -> C
BC -> H
KS -> H
PV -> O
KO -> K
OK -> H
OH -> H
BH -> F
NB -> B
FH -> N
HV -> F
BN -> S
ON -> V
CB -> V
CF -> H
FB -> S
KF -> S
PS -> P
OB -> C
NN -> K
KV -> C
BK -> H
SN -> S
NC -> H
PK -> B
PC -> H
KN -> S
VO -> V
FO -> K
CH -> B
PH -> N
SO -> C
KH -> S
HB -> V
HH -> B
BB -> H
SC -> V
HS -> K
SP -> V
KB -> N
VN -> H
HK -> H
KP -> K
OP -> F
CO -> B
VP -> H
OS -> N
OF -> H
KK -> N
CC -> K
BS -> C
VV -> O
CN -> H
PB -> P
BO -> N
SB -> H
FP -> F
SK -> F
PO -> S
KC -> H
VC -> H
NV -> N
HF -> B
PN -> F
SV -> K
PP -> K
"""

def parse(text):
    sec = text.split('\n\n')
    assert len(sec) == 2
    base = sec[0].strip()
    combos = [l for l in sec[1].split('\n') if l.strip()]
    mapping = dict()
    for c in combos:
        match c.split(' -> '):
            case [pair, subst]:
                match list(pair):
                    case [l, r]:
                        mapping[ (l,r) ] = subst
    print(len(mapping.keys()))
    return base, mapping


def score(out, last):
    pprint.pprint(out)
    edges= out
    proj = Counter([last])
    for (a,b), n in edges.items():
        proj[a] += n
    pprint.pprint(proj)
    values = proj.values()
    least = min(values)
    most = max(values)
    print(most - least)
    return most - least

def expand_counts(seq, mapping ,generations):
    prev = None
    edges = Counter()
    for i in range(len(seq)):
        if prev:
            edges[ (prev, seq[i])] += 1
        prev = seq[i]
    print('start on', seq, 'is', edges)
    score(edges, seq[-1])
    pprint.pprint(edges)
    for g in range(generations):
        out = Counter()
        for (start, end), n in list(edges.items()):
            print('there are', n, 'transitions from', start, 'to', end)
            ins = mapping[ (start, end)]
            print('now there are', n, 'transitions from', start, 'to', ins, 'and from', ins, end)
            out[ (start,ins) ] += n
            out[ (ins,end) ] += n
        print('after generation', g)
        score(out, seq[-1])
        edges = out

    return score(edges, seq[-1])


sample_base, sample_mapping = parse(sample)
assert sample_base == 'NNCB'
assert len(sample_mapping.keys()) == 16
assert sample_mapping[('B', 'C')] == 'B'

sample_answer = expand_counts(sample_base, sample_mapping, 10)

assert sample_answer == 1588

real_base, real_mapping = parse(real)
real_answer = expand_counts(real_base, real_mapping, 10)
assert real_answer == 2937

big_outseq = expand_counts(real_base, real_mapping, 40)
assert big_outseq == 3390034818249
