"""

Is there a closed form?

X progression = sum of natural numbers up to initial velocity = n*(n+1) / 2

so for good velocity we want to be falling straight down in [x0, x1]

so we can solve as 

x = n*(n+1)/2
2x = n*(n+1)
2x = n^2 + n
n^2 = (x -n)/2
n ~= sqrt(2x )


[part 2]
That only gives us a lower bound on the speed we can use
"""


# sample x=20..30, y=-10..-5
# real target area: x=34..67, y=-215..-186
from math import sqrt, ceil

def find_nearest_sum(x):
    limit = ceil(sqrt(x*2))
    v = limit
    prev = None
    while v > 0:
        sum = (v*(v+1))//2
        print(v, sum, prev)
        if (prev is not None and prev > x) and sum < x:
            print('nearest natural than sums to', x, 'is', v+1)
            return v+1
        v -= 1
        prev = sum

find_nearest_sum(20)


def simulate(x0, x1, y0, y1):
    all_maxy = 0
    speed0 = find_nearest_sum(min(x0,x1))
    speed1 = find_nearest_sum(max(x0,x1))
    speeds = list(range(speed0-1, x1+1))
    print('trying  X speeds', speeds)
    count = 0
    for ivx in speeds:
        for ivy in range(-1000, 1000):
            vx = ivx
            vy = ivy
            #print('fire at', ivx, ivy)
            x = 0
            y = 0
            maxy = y
            while x <= x1 and y >= min(y0, y1):
                x += vx
                y += vy 
                maxy = max(y, maxy)
                if vx>0 :
                    vx -= 1
                vy -= 1
                inside = x >= x0 and x <= x1 and y >= y0 and y <= y1
                #print('pos',x,y, 'vel', vx, vy, 'inside' if inside else 'outside')
                if inside:
                    all_maxy= max(maxy, all_maxy)
                    print('inital', ivx, ivy, 'works maxy', maxy, 'best yet', all_maxy)                                        
                    count += 1
                    break
        
            #print()
    return all_maxy, count

r = simulate(20, 30, -10, -5)
assert r == (45, 112)

# real target area: x=34..67, y=-215..-186
r2 = simulate(34, 67, -215, -186)
print(r2)
assert r2 == (23005, 2040)




"""