from collections import Counter
sample='3,4,3,1,2'
data='1,3,4,1,1,1,1,1,1,1,1,2,2,1,4,2,4,1,1,1,1,1,5,4,1,1,2,1,1,1,1,4,1,1,1,4,4,1,1,1,1,1,1,1,2,4,1,3,1,1,2,1,2,1,1,4,1,1,1,4,3,1,3,1,5,1,1,3,4,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,5,2,5,5,3,2,1,5,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,5,1,1,1,1,5,1,1,1,1,1,4,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,3,1,2,4,1,5,5,1,1,5,3,4,4,4,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,5,3,1,4,1,1,2,2,1,2,2,5,1,1,1,2,1,1,1,1,3,4,5,1,2,1,1,1,1,1,5,2,1,1,1,1,1,1,5,1,1,1,1,1,1,1,5,1,4,1,5,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,5,4,5,1,1,1,1,1,1,1,5,1,1,3,1,1,1,3,1,4,2,1,5,1,3,5,5,2,1,3,1,1,1,1,1,3,1,3,1,1,2,4,3,1,4,2,2,1,1,1,1,1,1,1,5,2,1,1,1,2'

def parse(sample):
    return [int(x) for x in sample.strip().split(',')]

state = parse(sample)
assert state[1] == 4
assert len(state) == 5

def simulate(state, days):
    statecounts = Counter()
    for v in state:
        statecounts[v] += 1
    
    for day in range(days):
        print('before', day, 'state counts', statecounts)
        newstate = Counter()
        for counter, value in statecounts.items():
            if counter == 0:
                newstate[6] += value
                newstate[8] += value
            else:
                newstate[counter-1] += value
            statecounts = newstate
        print('after', statecounts)
    return sum(statecounts.values())

assert simulate(state, 1) == 5
assert simulate(state, 2) == 6
assert simulate(state, 18)  == 26
assert simulate(state, 80) == 5934

print(simulate(parse(data), 80))
print(simulate(parse(data), 256))
