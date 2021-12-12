import pprint
sample="""start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
sample2="""dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
sample3="""fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""
real="""start-kc
pd-NV
start-zw
UI-pd
HK-end
UI-kc
pd-ih
ih-end
start-UI
kc-zw
end-ks
MF-mq
HK-zw
LF-ks
HK-kc
ih-HK
kc-pd
ks-pd
MF-pd
UI-zw
ih-NV
ks-HK
MF-kc
zw-NV
NV-ks"""
def parse(text):
    edges= {}
    for a, b in  [tuple(line.split('-')) for  line in text.split('\n')]:
        edges.setdefault(a, [])
        if b not in edges[a]:
            edges[a].append(b)
        edges.setdefault(b, [])
        if a not in edges[b]:
            edges[b].append(a)
    return edges

def walk(graph, path=[], results=[], twice=False):
    #print('at', path)
    if path[-1] == 'end':
        #print('path', path)
        results.append(path)
        return
    for out in graph[path[-1]]:
        if out[0].isupper() or out not in path:
            walk(graph, path+[out], results, twice)
        elif twice and not out[0].isupper() and out != 'start' and out != 'end':
                walk(graph, path+[out], results, False)

sample_graph = parse(sample)
pprint.pprint(sample_graph)
r = []
walk(sample_graph ,['start'], r)
pprint.pprint(r)
print(len(r))
assert len(r) == 10
r2 = []
walk(parse(sample2), ['start'], r2)
pprint.pprint(r2)
print(len(r2))
assert len(r2) == 19
r3 = []
walk(parse(sample3), ['start'], r3)
print(len(r3))
assert len(r3) == 226
r4 = []
walk(parse(real), ['start'], r4)
assert len(r4) == 4720
r1p = []
print()
print()

walk(parse(sample),['start'], r1p, True)
pprint.pprint(r1p)
print(len(r1p))
assert len(r1p) == 36
rp = []
walk(parse(real),['start'], rp, True)
print(len(rp))
assert len(rp) == 147848

