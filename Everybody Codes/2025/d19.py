DAY,_,_=__file__.rpartition('.')

from itertools import product
from collections import defaultdict
import heapq
import re

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall(r'-?\d+',l))]
        r+=[l]
        
D={}
for a,b,c in r:
    if a not in D:D[a]=[]
    D[a]+=[b,c],
e=max(D)

def dijkstra(init):
    distances = defaultdict(lambda: 1e99)
    q=[]
    s=set()
    for v in init:
        distances[v]=1
        heapq.heappush(q, (0, v))
    while q:
        d,(x,y) = heapq.heappop(q)
        s|={(x,y)}
        if x>=e:
            print(d)
            return
        if d >= distances[(x,y)]:
            continue
        for dy in (-1,1):
            Y=y+dy
            X=x+1
            if X in D:
                if not any(a<=Y<a+b for a,b in D[X]):
                    continue
            elif Y<0:continue
            if (X,Y) not in s:
                s|={(X,Y)}
                heapq.heappush(q, (d+(dy>0), (X,Y)))

dijkstra([(0,0)])


# ---


r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall(r'-?\d+',l))]
        r+=[l]

D={}
for a,b,c in r:
    if a not in D:D[a]=[]
    D[a]+=[b,c],
e=max(D)

dijkstra([(0,0)])


# --

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall(r'-?\d+',l))]

        r+=[l]

D={}
for a,b,c in r:
    if a not in D:D[a]=[]
    D[a]+=[b,c],
e=max(D)

H={}
for a,l in D.items():
    H[a]=[]
    for y,h in l:
        H[a]+=range(y,y+h)

q={0:0}
x=0
for (x1,l1) in sorted(H.items()):
    q2={}
    w=x1-x
    x=x1
    for (h1,v),h2 in product(q.items(),l1):
        d=abs(h1-h2)
        if d>w:continue
        if d%2 != w%2: continue
        m=v+(w+h2-h1)//2
        q2[h2] = min(m,q2.get(h2,1e9))

    q=q2
    print(end='.')
print
print(min(q.values()))