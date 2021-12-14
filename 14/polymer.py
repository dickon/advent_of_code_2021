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

def decompress(in_seq):
    seq = []
    for (ch, rep) in in_seq:
        seq += ch*rep
    return ''.join(seq)

def compress(in_seq):
    seq = decompress(in_seq)

    i = 0
    outseq_compressed = []
    print('compressing', seq)
    while i < len(seq):
        print('max seq len', len(seq)//2)
        take = 1
        repeats = 1
        for k in range(2, len(seq)//2):
            pattern = seq[i:i+k]
            hit = False
            print('check', pattern)
            if pattern == seq[i+k:i+k*2]:
                # got a repeat; how many repeats?
                n = 0
                while pattern == seq[i+k*n:i+k*(n+1)]:
                    n += 1
                if n >= 2:
                    print(n,'repeats of', pattern, 'at', i)
                    outseq_compressed.append ( (pattern, n))
                    take = k
                    repeats = n
                    break
            if take > 1:
                break
        
        outseq_compressed.append( (seq[i:i+take], repeats))
        i += take * repeats
    print(seq,'compresses to', outseq_compressed)
    return outseq_compressed
    
def expand(seq, mapping, generations):
    print('start', seq)
    def iterate(seq, generations):
        print('expand', seq, generations, 'times')
        for j in range(generations):
            print('generation', j, 'sequence', seq)
            # first do the transformation
            outseq = []
            prev = None
            outseq = []
            for (rec, n) in seq:
                recfirst = ''
                # first repetition is different since the predecessor coming in matters
                for i in range(0, len(rec)):
                    if prev:
                        recfirst += mapping[ (prev, rec[i])]
                    recfirst += rec[i]
                    prev = rec[i]
                # second onwards repetition uses the tail of the sequence as predecessor
                if n > 1:
                    recsecond = ''
                    prev = rec[-1]
                    for i in range(0, len(rec)):
                        recsecond += mapping[ (prev, rec[i])]
                        prev = rec[i]
                        recsecond += rec[i]
                else:
                    recsecond = ''
                if n== 1 or recfirst == recsecond :
                    outseq.append( (recfirst, n))
                else:
                    outseq += [(recfirst, 1), (recsecond, n-1)]
            print('new sequence', outseq)
            # second compress the sequence by spotting repetitions

            total_length= sum( [len(pat)*n for (pat,n) in seq])
            def advance(pos):
                if pos[0] > len(seq):
                    return
                rec = seq[pos[0]]
                if pos[1]+1 < len(rec[0])*rec[1]:
                    return (pos[0], pos[1]+1)
                else:
                    if pos[0]+1 >= len(seq):
                        return                    
                    return(pos[0]+1, 0)
            def lookup(pos):
                rec = seq[pos[0]]
                return rec[0][pos[1] // rec[1]]
            
            print()
            print()
            print('compression total length', total_length)
            while True:
                found = False
                for length in reversed(range(2, total_length//2+2)):
                    pos = (0,0)
                    while pos:
                        #print()
                        #print('finding pattern starting', pos, 'length' ,length)
                        # ... of certain length
                        pattern = ''
                        cursor = pos
                        ended = False
                        for i in range(length):
                            #print('build pattern cursor', cursor)
                            pattern += lookup(cursor)
                            cursor = advance(cursor)
                            if cursor is None:
                                ended = True
                                break
                        if ended:
                            break

                        #print('are there repetitions of', pattern, 'starting', cursor)
                        good = True
                        reps = 1
                        while True:
                            for i in range(length):
                                if lookup(cursor) == pattern[i]:
                                    #print('okay at', cursor)
                                    pass
                                else:
                                    #print('mismatch at', cursor)
                                    good = False
                                    break
                                cursor = advance(cursor)
                                if cursor is None: # fall off end?
                                    good = False
                                    break
                            if not good:
                                break
                            reps += 1
                            print('************** complete repetition of', pattern, 'from', pos, 'ending at', cursor, 'now found', reps, 'repetitions, in', seq)
                            # need to reform with repetition pulled out
                            found = False
                    
                        pos = advance(pos)
                        if found:
                            break
                if not found:
                    break

            if False:
                outseq_compressed = compress(outseq)
                print('after', j+1, 'generations seq', outseq_compressed)
                print(outseq_compressed)
                seq = outseq_compressed
            else:
                seq = outseq
        print('result', seq)
        return seq
    seq = iterate( [(seq, 1)], generations)
    return delta(seq)


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
    
def expand_fast(seq, mapping, generations):
    """
    Can we memoize? Can we work out a closed form?

    Is it possible for a sequence of a specific length X...Y  to have different counts depending what's in the middle? 
    Yes, even in this example (e.g. NCCN and NBBN). So we can't memoize on start, end and the length.

    How about if we memoize on start, end and counts? That seems like it might work but it may well not, since the expansion
    is order dependent. XY does not necessarily have the same mapping as YX.

    Given a starting adjacent pair e.g. NN nothing outside that pair has any effect

    NN
    NCN
    NBCCN
    NBBBCNCCN

    How about representation?

    store cache answers in a compact form with just what we need to know

    NN => (N, N, {'N':2})
    NCN => (N, N, {'N': 2, 'C', 1}
    NBCCN = (N, N, {'N', 2, 'C': 2, 'B': 1})


    Specific closed forms

                      start NNCB
    after 1 generations seq NCNBCHB
    after 2 generations seq NBCCNBBBCBHCB
    after 3 generations seq NBBBCNCCNBBNBNBBCHBHHBCHB
    after 4 generations seq NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
    after 5 generations seq NBBNBBNBBBNBBNBBCNCCNBBBCCNBCNCCNBBNBBNBBNBBNBBNBNBBNBBNBBNBBNBBCHBHHBCHBHHNHCNCHBCHBNBBCHBHHBCHB
    after 6 generations seq NBBNBBNBBNBBNBBNBNBBNBBNBBNBBNBBCCNBCNCCNBBNBNBBCNCCNBBBCCNBCNCCNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBCBHCBHHNHCBBCBHCBHHNHCNCHBCCNBCBHCBBCBHCBBNBBNBBCBHCBHHNHCBBCBHCB
    after 7 generations seq NBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBCNCCNBBBCCNBCNCCNBBNBBNBBBNBBNBBCCNBCNCCNBBNBNBBCNCCNBBBCCNBCNCCNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBCHBHHBCHBHHNHCNCHBCHBNBBCHBHHBCHBHHNHCNCHBCCNBCBHCBBCNCCNBBBCHBHHBCHBNBBCHBHHBCHBNBBNBBNBBNBBNBBCHBHHBCHBHHNHCNCHBCHBNBBCHBHHBCHB
    after 8 generations seq NBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBCCNBCNCCNBBNBNBBCNCCNBBBCCNBCNCCNBBNBBNBBNBBNBBNBNBBNBBNBBNBBNBBCNCCNBBBCCNBCNCCNBBNBBNBBBNBBNBBCCNBCNCCNBBNBNBBCNCCNBBBCCNBCNCCNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBCBHCBHHNHCBBCBHCBHHNHCNCHBCCNBCBHCBBCBHCBBNBBNBBCBHCBHHNHCBBCBHCBHHNHCNCHBCCNBCBHCBBCNCCNBBBCHBHHBCHBNBBCCNBCNCCNBBNBNBBCBHCBHHNHCBBCBHCBBNBBNBBCBHCBHHNHCBBCBHCBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBCBHCBHHNHCBBCBHCBHHNHCNCHBCCNBCBHCBBCBHCBBNBBNBBCBHCBHHNHCBBCBHCB





    NBBN -> NBBNBBN in one 1 step, NBBNBBNBBNBBN in 2 steps
    so NBBN = N(B^(x^2) 
    If we have a sequence such as NBBN and we know it expands to NBBNBBN then NBBNBBNBBNBBN 


    Idea: any repeating pattern would be better stored as a repeat

    so write NBBNBBN as (NBB)^2 N

                      start NNCB
    after 1 generations seq NCNBCHB
    after 2 generations seq NBCCNBBBCBHCB
    after 3 generations seq NBBBCNCCNBBNBNBBCHBHHBCHB
    after 4 generations seq NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
    after 5 generations seq (NBB)^3 B (NBB)^2 CNCCNBBBCCNBCNCCNBBNBBNBBNBBNBBNBNBBNBBNBBNBBNBBCHBHHBCHBHHNHCNCHBCHBNBBCHBHHBCHB
    after 6 generations seq (NBB)^4 NB (NBB)^4 CCNBCNCC NBB NB NBB CNCC NBB BCCNBCNCC (NBB)^10 B NBBNBBNBBNBBNBBNBBNBBNBBNBBNBBCBHCBHHNHCBBCBHCBHHNHCNCHBCCNBCBHCBBCBHCBBNBBNBBCBHCBHHNHCBBCBHCB
    after 7 generations seq NBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBCNCCNBBBCCNBCNCCNBBNBBNBBBNBBNBBCCNBCNCCNBBNBNBBCNCCNBBBCCNBCNCCNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBCHBHHBCHBHHNHCNCHBCHBNBBCHBHHBCHBHHNHCNCHBCCNBCBHCBBCNCCNBBBCHBHHBCHBNBBCHBHHBCHBNBBNBBNBBNBBNBBCHBHHBCHBHHNHCNCHBCHBNBBCHBHHBCHB
    after 8 generations seq NBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBCCNBCNCCNBBNBNBBCNCCNBBBCCNBCNCCNBBNBBNBBNBBNBBNBNBBNBBNBBNBBNBBCNCCNBBBCCNBCNCCNBBNBBNBBBNBBNBBCCNBCNCCNBBNBNBBCNCCNBBBCCNBCNCCNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBCBHCBHHNHCBBCBHCBHHNHCNCHBCCNBCBHCBBCBHCBBNBBNBBCBHCBHHNHCBBCBHCBHHNHCNCHBCCNBCBHCBBCNCCNBBBCHBHHBCHBNBBCCNBCNCCNBBNBNBBCBHCBHHNHCBBCBHCBBNBBNBBCBHCBHHNHCBBCBHCBBNBBNBBNBBNBBNBBNBBNBBNBBNBBNBBCBHCBHHNHCBBCBHCBHHNHCNCHBCCNBCBHCBBCBHCBBNBBNBBCBHCBHHNHCBBCBHCB



    If we have a sequence X...Y and we know the counts  already know what a step on that will
    """
    print('start', seq)

    # for j in range(generations):
    #     outseq = ''
    #     for i in range(len(seq)-1):
    #         n = mapping[ (seq[i], seq[i+1])]
    #         outseq += seq[i] + n
    #     outseq += seq[-1]
    #     print('after', j+1, 'generations seq', outseq)
    #     for i in range(len(seq)-1):
    #         for k in range(2, len(seq)//2):
    #             if seq[i:i+k] == seq[i+k:i+k*2]:
    #                 print(k, 'repeat of', pattern, 'at', i)
    #             else:
    #                 break
    #     seq = outseq
    # return delta(outseq)


def delta(seq):
    counts = Counter(seq)
    values = counts.values()
    least = min(values)
    most = max(values)
    return most - least

sample_base, sample_mapping = parse(sample)
assert sample_base == 'NNCB'
assert len(sample_mapping.keys()) == 16
assert sample_mapping[('B', 'C')] == 'B'

sample_answer = expand_counts(sample_base, sample_mapping, 10)

#sample_answer = expand(sample_base, sample_mapping, 10)

assert sample_answer == 1588

#expand('NN', sample_mapping, 10)

real_base, real_mapping = parse(real)
#real_answer = expand(real_base, real_mapping, 10)
real_answer = expand_counts(real_base, real_mapping, 10)
#expand_counts(real_base, real_mapping, 10)
assert real_answer == 2937
#print(real_answer)

big_outseq = expand_counts(real_base, real_mapping, 40)
#big_answer = delta(big_outseq)
#print(big_answer)
