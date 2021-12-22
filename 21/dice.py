from functools import cache
from collections import Counter
from pprint import pprint

def run(p1, p2, dice):
    pos = [p1-1, p2-1]
    score = [0,0]
    s1 = s2 = 0
    i = 0
    while True:
        for p in range(2):
            for throws in range(3):
                pos[p] = (pos[p] + dice[i % len(dice)]) % 10
                i += 1
            score[p] += pos[p] + 1
            #print(score, 'after', i, 'throws')
            if score[p]>= 1000:
                print('player',p,'wins')
                print('score', score[(p+1)%2] * i)
                return

run(4, 8, range(1,101))
run(7, 5, range(1,101))

def replace(tup, field, value):
    l = list(tup)
    l[field] = value
    return tuple(l)


outcomes = Counter()
for r1 in range(1,4):
    for r2 in range(1,4):
        for r3 in range(1,4):
            tot = r1+r2+r3
            outcomes[tot] += 1

pprint(outcomes)
def start2(start=(4,8), goal=1000, verbose=False):

    print()
    print('playing with start', start, 'goal', goal)
    @cache
    def run2(score_t, pos_t, round):
        p = round % 2
        wins = [0, 0]
        
        for tot, count in outcomes.items():
            pos_t2 = replace(pos_t, p, (pos_t[p] + tot)%10 )
            score_t2 = replace(score_t, p, score_t[p]+pos_t2[p]+1)
            if verbose:
                print('after turn', p, 'from scores', score_t, 'rolling',tot,'scores', score_t2, 'pos', pos_t2)
            if score_t2[p] >= goal:
                if verbose:
                    print('player', p, 'wins!')
                wins[p] += count
            else:
                assert score_t2[0] < goal
                assert score_t2[1] < goal
                if verbose:
                    print('recursing with', score_t2, pos_t2,'to run round', round+1)
                nwins = run2(score_t2, pos_t2, (round+1)%2)
                wins[0] += nwins[0] * count
                wins[1] += nwins[1] * count
        if verbose:
            print('from scores', score_t, 'at pos', pos_t, 'wins are', wins)
        return wins

    start_pos = ( (start[0]-1, start[1]-1))
    return run2( (0,0), start_pos,  0)

assert start2(goal=3, verbose=True) == [990, 207]
assert start2(start=(0,0), goal=3, verbose=True) == [27, 0]
for pos in [(4,8), (7,5)]:
    r = start2(start=pos, goal=21, verbose=False)
    print(pos, r)
    if pos == (4,8):
        assert r == [444356092776315,341960390180808]

            