sample = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

def lex(text):
    return [ line.split() for line in text.split('\n')]

def parse(lexemes):
    return [ (spl[0], int(spl[1])) for spl in lexemes if len(spl) == 2 ] # might throw if non-number in second field

assert(len(parse(lex(sample))) == 6)
assert(parse(lex(sample))[2] == ('forward', 8))

actions = {
    'forward': (1,0),
    'down':(0, 1),
    'up':(0, -1),
}

def execute(instructions):
    position = (0,0)
    for action, amount in instructions:
        vec = actions.get(action)
        if vec is None:
            print('ERROR: BAD ACTION', action)
        else:
            position = (position[0] + vec[0]*amount, position[1] + vec[1]*amount)
    return position

assert(execute(parse(lex(sample))) == (15,10))

data_tokens = parse(lex(open('2/data.txt', 'r').read()))
res = execute(data_tokens)
assert(res == (2073, 850))
print(res, res[0]*res[1])


def execute2(instructions):
    distance = 0
    depth = 0
    aim = 0

    for action, amount in instructions:
        if action == 'down':
            aim += amount
        elif action == 'up':
            aim -= amount
        elif action == 'forward':
            distance += amount
            depth += aim * amount
        else:
            print('ERROR: BAD ACTION')
    return (distance, depth)

assert(execute2(parse(lex(sample))) == (15, 60))

res2 = execute2(data_tokens)
print(res2, res2[0] * res2[1])
print('end')


    