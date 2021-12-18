from math import ceil, floor
realdata = """[[6,[[9,4],[5,5]]],[[[0,7],[7,8]],[7,0]]]
[[[[2,1],[8,6]],[2,[4,0]]],[9,[4,[0,6]]]]
[[[[4,2],[7,7]],4],[3,5]]
[8,[3,[[2,3],5]]]
[[[[0,0],[4,7]],[[5,5],[8,5]]],[8,0]]
[[[[5,2],[5,7]],[1,[5,3]]],[[4,[8,4]],2]]
[[5,[[2,8],[9,3]]],[[7,[5,2]],[[9,0],[5,2]]]]
[[9,[[4,3],1]],[[[9,0],[5,8]],[[2,6],1]]]
[[0,6],[6,[[6,4],[7,0]]]]
[[[9,[4,2]],[[6,0],[8,9]]],[[0,4],[3,[6,8]]]]
[[[[3,2],0],[[9,6],[3,1]]],[[[3,6],[7,6]],[2,[6,4]]]]
[5,[[[1,6],[7,8]],[[6,1],[3,0]]]]
[2,[[6,[7,6]],[[8,6],3]]]
[[[[0,9],1],[2,3]],[[[7,9],1],7]]
[[[[1,8],3],[[8,8],[0,8]]],[[2,1],[8,0]]]
[[2,9],[[5,1],[[9,3],[4,0]]]]
[9,[8,4]]
[[[3,3],[[6,2],8]],5]
[[[9,[4,8]],[[1,3],[6,7]]],[9,[[4,4],2]]]
[[[[1,3],6],[[5,6],[1,9]]],[9,[[0,2],9]]]
[7,[[[0,6],[1,2]],4]]
[[[[5,0],[8,7]],[[7,3],0]],[[6,7],[0,1]]]
[[[[5,4],7],[[8,2],1]],[[[7,0],[6,9]],0]]
[[[3,[5,6]],[[9,5],4]],[[[9,4],[8,1]],[5,[7,4]]]]
[[[3,[7,5]],[[8,1],8]],[[[6,3],[9,2]],[[5,7],7]]]
[8,[[2,0],[[2,6],8]]]
[[[[5,8],9],1],[9,6]]
[[[9,9],[8,8]],[[[3,5],[8,0]],[[4,6],[3,2]]]]
[[5,[[5,1],6]],[[5,8],9]]
[[7,[[1,6],6]],[[[8,6],7],[6,6]]]
[[0,[[9,5],0]],[4,[[7,9],[4,9]]]]
[[[[4,3],[3,5]],[[1,9],[7,6]]],[3,[[6,4],[6,0]]]]
[[[2,6],6],[6,3]]
[[[[1,5],[3,7]],0],[3,7]]
[4,[[[5,5],4],[[5,5],[9,3]]]]
[[3,[8,6]],[8,[7,7]]]
[8,[9,5]]
[[[6,3],[2,[3,6]]],[[[6,0],[0,2]],[[8,7],5]]]
[[[8,[1,2]],2],7]
[[[[8,4],[2,7]],[[3,9],7]],[[4,[8,8]],[[7,4],9]]]
[[[8,[2,5]],[3,[1,2]]],[[4,[5,0]],3]]
[[8,[0,3]],[[5,1],[1,1]]]
[[[8,[3,6]],6],[[7,[1,5]],[[4,8],9]]]
[[[5,0],[0,3]],[[2,[7,8]],[1,[4,8]]]]
[9,[4,[9,4]]]
[[[9,[0,4]],2],3]
[[9,[7,[8,9]]],3]
[[[8,6],[[3,5],[9,2]]],[[3,[9,7]],5]]
[[6,[[7,4],2]],[2,[7,[6,0]]]]
[1,[[[2,2],6],8]]
[[[6,[1,8]],[[9,3],[1,8]]],[[[8,2],[9,3]],[[8,2],[9,9]]]]
[[[[2,9],[1,7]],[[4,0],8]],[[8,9],[6,3]]]
[[[[2,4],[6,1]],[[5,4],[2,8]]],[8,[1,[2,4]]]]
[[[4,6],[1,6]],[3,[1,1]]]
[[[[8,3],8],8],[1,[[4,2],3]]]
[[[9,[8,7]],[5,9]],[8,[[5,6],[4,5]]]]
[[[[4,1],2],[[7,8],4]],[0,6]]
[[[9,7],[[8,6],[6,9]]],[[8,[8,4]],[[9,0],2]]]
[[[8,5],[1,9]],[[[2,4],5],6]]
[[[9,[9,3]],[9,[2,3]]],[7,7]]
[[[8,[7,4]],[2,6]],[[[4,5],[9,9]],[0,[5,2]]]]
[7,[2,2]]
[[[[1,8],[5,2]],3],[0,[2,[4,5]]]]
[[5,[[4,8],[5,5]]],[4,[[3,4],[6,0]]]]
[[3,1],[4,[3,[8,2]]]]
[[3,7],[3,[[6,1],[0,2]]]]
[[4,[6,2]],[[3,9],8]]
[[[[2,9],3],[[5,6],4]],[8,2]]
[[4,[[7,9],[4,9]]],[[4,3],[7,[0,7]]]]
[[[3,[8,9]],[[3,4],[9,5]]],3]
[0,[[[3,0],[8,7]],[[0,9],[9,1]]]]
[[[5,[9,9]],2],[4,8]]
[[[[4,4],4],5],[3,4]]
[[[3,[2,2]],7],[[3,2],0]]
[[[[0,5],[5,2]],2],[2,[[1,2],2]]]
[[[4,6],6],[[0,1],6]]
[2,[[[3,9],7],[[9,8],8]]]
[[7,9],[7,[[3,0],9]]]
[[[1,[6,2]],[0,8]],[[[7,2],4],9]]
[[[[4,7],[1,5]],[5,9]],[[2,[0,4]],[7,[7,0]]]]
[[1,[[2,0],[0,4]]],[[[4,6],9],[[6,8],[0,1]]]]
[[[[6,0],7],[7,[9,6]]],[[7,[4,9]],[9,4]]]
[[[5,[4,6]],[[1,9],[5,8]]],[[[3,6],[2,6]],[[7,3],7]]]
[[[6,0],[6,6]],[2,8]]
[[[4,[7,2]],[[5,6],[2,4]]],[[[6,8],5],[4,6]]]
[[[[9,0],9],[4,0]],[[[9,1],8],[6,4]]]
[[6,3],[1,[[5,0],[9,9]]]]
[[[2,7],[5,6]],[[6,[1,4]],[9,9]]]
[[[[0,5],3],[8,7]],[[[9,9],[6,2]],[0,7]]]
[[[5,6],[1,7]],[[[0,4],9],9]]
[[[7,3],3],[6,[0,[8,9]]]]
[[[0,6],[[8,5],[4,6]]],[[[2,7],[4,2]],[[8,7],[0,5]]]]
[[[8,[7,3]],1],8]
[[8,[8,[8,2]]],[[5,4],[1,[2,6]]]]
[[[[1,1],[8,6]],5],9]
[[[[2,4],[5,7]],[[5,8],[3,1]]],7]
[[4,[[0,1],9]],[[3,8],[4,2]]]
[3,2]
[[3,4],[8,[[6,5],[6,6]]]]
[[[[7,0],[3,8]],[[3,3],[2,6]]],[[8,0],9]]"""

class Action(Exception):
    pass

class Pair:
    def __init__(self, x, y, up=None, depth=0):
        self.x = x
        self.y = y
        self.up = up
        self.depth = depth
        self.lhs = False
        self.rhs = False
    def top(self):
        if self.up:
            return self.up.top()
        else:
            return self
    def __repr__(self):
        return '['+repr(self.x)+','+repr(self.y)+']'
    def dump(self):
        return '['+self.x.dump()+', '+self.y.dump()+']'
    def setdepth(self, depth=0, sequence=0):
        self.depth = depth
        self.x.up = self
        self.y.up = self
        self.x.lhs = True
        self.x.rhs = False
        self.y.lhs = False
        self.y.rhs = True
        seq2 = self.x.setdepth(depth+1, sequence)
        seq3 = self.y.setdepth(depth+1, seq2)
        return seq3
    def maybe_explode(self):
        if self.depth >= 4 and isinstance(self.x, Int) and isinstance(self.y, Int):
            top = self.top()
            prev = top.find_by_sequence(self.x.sequence - 1)
            next = top.find_by_sequence(self.y.sequence + 1)
            #print('explode', self.dump(), 'in', top.dump(), 'lhs', self.lhs, 'rhs', self.rhs, 'prev', prev, 'next', next)
            if prev:
                prev.v += self.x.v
            if next: 
                next.v += self.y.v            
            zero = Int(0)
            if self.lhs:
                self.up.x = zero
            if self.rhs:
                self.up.y = zero
            self.top().setdepth()
            #print('new structure', self.top())
            raise Action()
        else:
            self.x.maybe_explode()
            self.y.maybe_explode()
    def maybe_split(self):
        self.x.maybe_split()
        self.y.maybe_split()
        
    def find_by_sequence(self, x):
        a = self.x.find_by_sequence(x)
        b = self.y.find_by_sequence(x)
        return a if a is not None else b
    def magnitude(self):
        return 3*self.x.magnitude() + 2*self.y.magnitude()

class Int:
    def __init__(self, v):
        self.v = v
        self.up = None
        self.depth = 0
        self.sequence = 0
        self.lhs = False
        self.rhs = False
    def dump(self):
        return f'v={self.v} depth={self.depth} sequence={self.depth}'
    def __repr__(self):
        return repr(self.v) 
    def setdepth(self, depth=0, sequence = 0):
        self.depth = depth
        self.sequence = sequence
        return sequence+1
    def maybe_explode(self):
        return
    def maybe_split(self):
        if self.v >= 10:
            half = self.v / 2
            n = Pair(Int(floor(half)), Int(ceil(half)))
            #print('split', self.dump(), 'to', n.dump())
            if self.lhs:
                self.up.x = n
            if self.rhs:
                self.up.y = n
            self.top().setdepth()
            raise Action()            
        else:
            return self
    def find_by_sequence(self, x):
        if self.sequence == x:
            return self        
    def top(self):
        if self.up:
            return self.up.top()
        else:
            return self
    def magnitude(self):
        return self.v

def tick(x):
    x.setdepth()
    try:
        x.maybe_explode()
    except Action:
        #print('explode happened')
        return 'explode'
    try:
        x.maybe_split()
    except Action:
        #print('split happened')
        return 'split'

def addup(seq):
    nums = [construct(x) for x in seq]
    acc = nums[0]
    for i in nums[1:]:
        acc = Pair(acc, i)
        loop(acc)
    return acc

def construct(l):
    if type(l) == type([]):
        lp = construct(l[0])
        lp.lhs = True
        rp = construct(l[1])
        rp.rhs = True
        p = Pair(lp, rp)
        lp.up = p
        rp.up = p
        return p
    elif type(l) == type(1):
        return Int(l)
    else:
        assert 0
    
def loop(l):
    while True:
        action = tick(l)
        if action is None:
            break
    return l

c1 = construct([[[[[9,8],1],2],3],4])    
c1.setdepth()
print(c1)
tick(c1)
assert repr(c1) == '[[[[0,9],2],3],4]'
v3 = construct([10,10])
tick(v3)
assert repr(v3) == '[[5,5],10]'

for before, after in [
    ([7,[6,[5,[4,[3,2]]]]], '[7,[6,[5,[7,0]]]]'),
    ([[6,[5,[4,[3,2]]]],1], '[[6,[5,[7,0]]],3]'),
    ([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] , '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'),
    ([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'),
]:
    t = construct(before)
    t.setdepth()
    print('before', t.dump())
    tick(t)
    print(repr(t))
    assert repr(t) == after

ex = construct([[[[[4,3],4],4],[7,[[8,4],9]]], [1,1]])
tick(ex)
print(repr(ex))
assert repr(ex) == '[[[[0,7],4],[7,[[8,4],9]]],[1,1]]'
a1 = tick(ex)
assert a1 == 'explode'
assert repr(ex) == '[[[[0,7],4],[15,[0,13]]],[1,1]]'
print()
print(ex)
a2 = tick(ex)
print(a2)
assert a2 == 'split'
assert repr(ex) == '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'
a3 = tick(ex)
assert a3 == 'split'
print(ex)
assert repr(ex) == '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]'
a4 = tick(ex)
assert a4 == 'explode'
print(ex)
assert repr(ex) == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'

r = addup([[1,1],
[2,2],
[3,3],
[4,4]])
print(r)
assert repr(r) == '[[[[1,1],[2,2]],[3,3]],[4,4]]'

v = addup([[1,1],
[2,2],
[3,3],
[4,4],
[5,5]])
assert repr(v) == '[[[[3,0],[5,3]],[4,4]],[5,5]]'

s = addup([[1,1],
[2,2],
[3,3],
[4,4],
[5,5],
[6,6]]
)
assert repr(s) == '[[[[5,0],[7,4]],[5,5]],[6,6]]'

print()
w = addup([ 
    [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],
[7,[5,[[3,8],[1,4]]]],
[[2,[2,2]],[8,[8,1]]],
[2,9],
[1,[[[9,3],9],[[9,0],[0,7]]]],
[[[5,[7,4]],7],1],
[[[[4,2],2],6],[8,7]]
])
print(w)
assert repr(w) == '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'

assert construct([[1,2],[[3,4],5]]).magnitude() == 143
assert construct([[[[0,7],4],[[7,8],[6,0]]],[8,1]]).magnitude() == 1384
assert construct([[[[1,1],[2,2]],[3,3]],[4,4]]).magnitude() == 445
assert construct([[[[3,0],[5,3]],[4,4]],[5,5]]).magnitude() == 791
assert construct([[[[5,0],[7,4]],[5,5]],[6,6]]).magnitude() == 1137
assert construct([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]).magnitude() == 3488

ans = addup([
    [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]],
[[[5,[2,8]],4],[5,[[9,9],0]]],
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]],
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]],
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]],
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]],
[[[[5,4],[7,7]],8],[[8,3],8]],
[[9,3],[[9,9],[6,[4,9]]]],
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]],
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]],
])
assert repr(ans) == '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]'
assert ans.magnitude() == 4140

expr = eval('['+realdata.replace('\n', ',\n')+']')
rans = addup(expr)
print(rans.magnitude())

biggest = 0
for x in expr:
    for y in expr:
        if x != y:
            m = addup([x,y]).magnitude()
            biggest = max(biggest, m)
print(biggest)
