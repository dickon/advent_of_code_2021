sample="""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
real = """
8271653836
7567626775
2315713316
6542655315
2453637333
1247264328
2325146614
2115843171
6182376282
2384738675"""

def parse(data):
    return [[int(x) for x in line.strip()] for line in data.split('\n') if line.strip()]

def foreach(data, op):
    for y in range(len(data)):
        for x in range(len(data[0])):
            op(x,y)

def render(data, highlight=(-1,-1)):
    for y in range(len(data)):
        ch = ''
        for x in range(len(data[0])):
            e = data[y][x]
            if e >= 10:
                if highlight == (x,y):
                    ch += '\033[94m\033[1m' + '*' + '\033[0m'
                else:
                    ch += '\033[1m' + '*' + '\033[0m'
            else:
                ch += str(e)
        print(ch)

def run(data, iterations=1, verbose=True):
    if verbose:
        print('start state')
        render(data)
    state = { 'flashes': 0 }
    sync = []
    for i in range(iterations):
        if verbose:
            print('round', i)
        def increment(x,y):
            data[y][x] += 1
        foreach(data, increment)
        if verbose:
            print('after increments')
            render(data)
        state['triggered'] = True
        j = 0
        state['flashed'] = set()
        while state['triggered']:
            state['triggered'] = False
            if verbose:
                print('cascade', j, 'state', state)
            j += 1
            def flash_if_triggered(x,y):
                if data[y][x] <= 9 or (x,y) in state['flashed']: return
                state['triggered'] = True
                state['flashes'] += 1
                state['flashed'].add(  (x,y))
                for dx in [-1,0,1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0: continue
                        xp = x + dx
                        yp = y + dy
                        if xp >= 0 and xp < len(data[0]) and yp >=0 and yp < len(data):
                            data[yp][xp] += 1
                if verbose:
                    print('flash', x, y, data[y][x], state)
                    render(data, (x,y))
            foreach(data, flash_if_triggered)
            if verbose:
                print('after triggering')
                render(data)
        def clear_flashed(x,y):
            if data[y][x] > 9:
                data[y][x] = 0
        if verbose:
            print(len(state['flashed']), 'flashed; clearing flashed on round', i+1)
        foreach(data, clear_flashed)
        if len(state['flashed']) == len(data) *len(data[0]):
            if verbose:
                print('synchronized at', i+1)
            sync.append(i+1)
        if verbose:
            print('post-round', i+1, 'state', state)
            render(data)
            print()
    return data, state['flashes'], sync

r1, _, _ = run(parse(sample), 1, False)
assert r1[0] == [6, 5, 9, 4, 2, 5, 4, 3, 3, 4]

r2, _, _ = run(parse(sample), 2, False)
assert r2[0] == [8,8,0,7,4,7,6,5,5,5]

r3, _, _ = run(parse(sample), 3, False)
assert r3[0] == [0,0,5,0,9,0,0,8,6,6]

_, flashes10, _ = run(parse(sample), 10, False)
assert flashes10 == 204

_, flashes100, _ = run(parse(sample), 100, False)
assert flashes100== 1656

run(parse(sample), 3)

_, flashes100real, _ = run(parse(real), 100, False)

print(flashes100real)

_, _, sync = run(parse(sample), 200, False)
assert sync[0] == 195

_, _, sync = run(parse(real), 500, False)
assert sync[0] == 268
