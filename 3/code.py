from collections import Counter
data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
def splitstrip(text):
    return [x.strip() for x in text.split('\n') if x.strip()]

def invert(x):
    return '0' if x == '1' else '1'

def countbit(textlist, field):
    c = Counter()
    for entry in textlist:
        c[entry[field]] += 1
    return c

def derive(textlist):
    gamma = ''
    episolon = ''
    for i in range(len(textlist[0])):
        c = countbit(textlist, i)
        popular = max(c, key=c.get)
        gamma += popular
        episolon += invert(popular)
    return gamma, episolon

def calc(totals):
    return int(totals[0], 2) * int(totals[1], 2)

def derive_lifesupport(textlist, most=True):
    working = textlist
    for i in range(len(textlist[0])):
        c = countbit(working, i)
        popular = '1' if c['1']>=c['0'] else '0'
        chosen = popular if most else invert(popular)
        working = [x for x in working if x[i] == chosen]
        if len(working) == 1:
            return int(working[0], 2)

def derive_co2(textlist):
    return derive_lifesupport(textlist, lambda c: '0' if c['0'] >= c['1'] else '1')

testdata = splitstrip(data)
assert derive(testdata) == ('10110', '01001')
assert calc(derive(testdata)) == 198

data = splitstrip(open('3/data.txt', 'r').read())
print(calc(derive(data)))

print(derive_lifesupport(testdata, True), derive_lifesupport(testdata, False))
print(derive_lifesupport(testdata, True), derive_lifesupport(testdata, False))
r = derive_lifesupport(data, True) * derive_lifesupport(data, False)
assert r == 6677951
print(r)
