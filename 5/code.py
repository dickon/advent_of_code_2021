from collections import Counter
import math
import numpy

sample = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
def parse_coords(t):
    return numpy.array([int(x) for x in t.split(',')])

def parse(text):    
    l =  [[parse_coords(x) for x in line.split(' -> ') if x] for line in text.split('\n')]
    return [i for i in l if i]

def analyse(lines, hv_only = True):
    counts = Counter()
    for points in lines:
        #print(points)
        cursor = points[0]
        vector = points[1] - points [0]
        length = numpy.linalg.norm(vector)
        unitv = vector / length
        if unitv[0] == 0 or unitv[1] == 0 or not hv_only:
            step = unitv if unitv[0] == 0 or unitv[1] == 0 else unitv * math.sqrt(2)
            while True:
                counts[(cursor[0], cursor[1])] += 1
                if numpy.linalg.norm((cursor - points[1])) < 0.1:
                    break
                cursor = numpy.add(cursor, step)
    r = len([x for x in counts.values() if x > 1])
    print('more than 1 at', r, 'locations', 'with', 4 if hv_only else 8)
    return r

sample_lines = parse(sample)
assert (sample_lines[0][0] == numpy.array([0,9])).all()
assert (sample_lines[0][1] == numpy.array([5,9])).all()
assert analyse(sample_lines) == 5

lines = parse(open('5/data.txt', 'r').read())
analyse(lines)
analyse(sample_lines, False)
assert analyse(sample_lines, False) == 12
analyse(lines, False)
