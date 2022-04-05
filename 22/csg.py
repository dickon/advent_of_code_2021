from pprint import pprint
ex1 = """on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10"""

def parse(text):
    cubes =[]
    for line in text.split('\n'):
        s = line.strip()
        if s == '':
            continue
        spaces = s.split()
        assert len(spaces) == 2
        sense = spaces[0]
        assert sense in ['on', 'off']
        cspl = spaces[1].split(',')
        assert len(cspl) == 3
        extents = []
        for i, dim in enumerate(cspl):
            espl = dim.split('=')
            assert len(espl) == 2
            [axis, vals] = espl
            assert axis in 'xyz'
            assert axis == 'xyz'[i]
            vl = [int(x) for x in vals.split('..')]
            extents.append(vl)
        a = extents[0][0], extents[1][0], extents[2][0]
        b = extents[0][1], extents[1][1], extents[2][1]
        cubes.append((sense, (a,b)))
    return cubes

ex1cubes = parse(ex1)
print(ex1cubes)

def segment(text):
    cubes = parse(text)
    # # skip over initial off cubes, since they are NOPs
    # i = 0
    # while cubes[i][0] == 'off':
    #     i += 1
    # if i == len(cubes):
    #     return []
    
    values = {0: set(), 1:set(), 2:set()}

    for _, coords in cubes:
        for coord in list(coords):
            for dim in range(3):
                values[dim].add(coord[dim]-1)
                values[dim].add(coord[dim])
                values[dim].add(coord[dim]+1)

    lit = 0
    sx = sorted(list(values[0]))
    sy = sorted(list(values[1]))
    sz = sorted(list(values[2]))
    states = {}
    for xi, x in enumerate(sx):
        for yi, y in enumerate(sy):
            for zi, z in enumerate(sz):
                active = 0
                for ci, (sense, coords) in enumerate(cubes):
                    if x >= coords[0][0] and x <= coords[1][0] and y >= coords[0][1] and y <= coords[1][1] and z >= coords[0][2] and z<=coords[1][2]:
                        if sense == 'on': 
                            active = 1
                        else:
                            active = 0
                states[ (x,y,z) ] = active
                print(f'{x},{y},{z} is {active} after applying cube {ci} {coords}')
                if xi > 0 and yi >0 and zi > 0:
                    prev = (sx[xi-1], sy[yi-1], sz[zi-1])
                    pactive = states[ prev ]
                    print(f'{prev} was active={pactive}')
                    if active and pactive:
                        n =  (1+x-prev[0])* (1+y-prev[1]) + (1+z-prev[2])
                        print('count cube', (prev), 'to', (x,y,z), 'as', n-1)
                        lit += n -1
                lit += active
    print('active', lit)
    return lit

assert segment(ex1) == 39

assert segment("""on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15""") == 590784




        