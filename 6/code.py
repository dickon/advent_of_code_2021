sample='3,4,3,1,2'
data='1,3,4,1,1,1,1,1,1,1,1,2,2,1,4,2,4,1,1,1,1,1,5,4,1,1,2,1,1,1,1,4,1,1,1,4,4,1,1,1,1,1,1,1,2,4,1,3,1,1,2,1,2,1,1,4,1,1,1,4,3,1,3,1,5,1,1,3,4,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,5,2,5,5,3,2,1,5,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,5,1,1,1,1,5,1,1,1,1,1,4,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,3,1,2,4,1,5,5,1,1,5,3,4,4,4,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,5,3,1,4,1,1,2,2,1,2,2,5,1,1,1,2,1,1,1,1,3,4,5,1,2,1,1,1,1,1,5,2,1,1,1,1,1,1,5,1,1,1,1,1,1,1,5,1,4,1,5,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,5,4,5,1,1,1,1,1,1,1,5,1,1,3,1,1,1,3,1,4,2,1,5,1,3,5,5,2,1,3,1,1,1,1,1,3,1,3,1,1,2,4,3,1,4,2,2,1,1,1,1,1,1,1,5,2,1,1,1,2'

def parse(sample):
    return [int(x) for x in sample.strip().split(',')]

state = parse(sample)
assert state[1] == 4
assert len(state) == 5

def simulate(state, days):
    for day in range(days):
        print(day)
        state = [x - 1 if x > 0 else 6 for x in state] + [8]*len([x for x in state if x == 0])
        #print(f'After {day+1} days: {",".join([str(x) for x in state])}')
    return state

assert simulate(state, 1) == [2,3,2,0,1]
assert simulate(state, 2) == [1,2,1,6,0,8]
assert len(simulate(state, 18))  == 26
assert len(simulate(state, 80)) == 5934

print(len(simulate(parse(data), 80)))
#print(len(simulate(parse(data), 256)))
