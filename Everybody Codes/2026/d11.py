DAY,_,_=__file__.rpartition('.')

from itertools import permutations
from math import inf
import re

def strain(N,e):
    d=[[inf]*N for _ in ' '*N]

    for p in range(N):
        d[p][p]=0
        q=[p]
        for c in q:
            for n in e.get(c,[]):
                if d[p][n] == inf:
                    d[p][n] = d[p][c]+1
                    q+=[n]
    return sum(sum(l)for l in d)

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall(r'-?\d+',l))]
        r+=[l]

(portals,),_,*r=r

e={}
for i in range(portals):
    e[i]=e.get(i,[])+[(i+1)%portals, (i-1)%portals]

N=portals

A=strain(N,e)
for a,b in r:
    a,b=a-1,b-1
    e[a] = e.get(a,[]) + [b]
    e[b] = e.get(b,[]) + [a]


B=strain(N,e)

print(A-B)

# -----

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall(r'-?\d+',l))]
        r+=[l]
        
(portals,),_,*r=r

e={}
for i in range(portals):
    e[i]=e.get(i,[])+[j%portals for j in range(i-3,i+4)if j!=i]

N=portals

A=strain(N,e)
for a,b in r:
    a,b=a-1,b-1
    e[a] = e.get(a,[]) + [b]
    e[b] = e.get(b,[]) + [a]

R=[]
for i in range(N):
    for j in range(N):
        if i!=j and j not in e[i]:
            e[i]+=[j]
            e[j]+=[i]
            R+=strain(N,e),
            e[i].pop()
            e[j].pop()

print(A-min(R))


# ----


r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall(r'-?\d+',l))]
        r+=[l]
        
(portals,),_,*r=r

e={}
for i in range(portals):
    e[i]=e.get(i,[])+[j%portals for j in range(i-3,i+4)if j!=i]

N=portals

A=strain(N,e)
for a,b in r:
    a,b=a-1,b-1
    e[a] = e.get(a,[]) + [b]
    e[b] = e.get(b,[]) + [a]

R=[]
combs = set()
w=N//8
for i in range(w):
    p=[*range(i,N,w)]
    for x in permutations(p):
        v=sorted(map(tuple,map(sorted,zip(*[iter(x)]*2))))
        combs.add(tuple(v))

for v in combs:
    for i,j in v:
        e[i]+=[j]
        e[j]+=[i]
    R+=strain(N,e),
    for i,j in v:
        e[i].pop()
        e[j].pop()

print(A-min(R))

