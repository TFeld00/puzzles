DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
from itertools import product
import re

def parse(part):
    r=[]

    with open(f'{DAY}{part}.txt','r')as F:
        for l in F:
            l=l.rstrip('\n')
            l=[*map(int,re.findall(r'-?\d+',l))]
            r+=[l]
    
    if part=='a':
        r = parse_no_headers(r)
        tests=[]
    else:
        *r,_,tests = parse_no_headers(r)

    F={}
    P={}
    E={}
    last=0
    for p,*b in r:
        v,w=p
        P[v]=w
        for q in b:
            if len(q)==1:
                F[v]=q[0]
            else:
                x,y=q
                if v not in E:
                    E[v]=[]
                E[v]+=[x,y],
        last = v
    return F,P,E,last,tests

def f(n):
    s=0
    if n in F:
        return F[n]
    for v,w in E[n]:
        s+=f(v)*w
    if s>=P[n]:
        return s
    return 0

# --

F,P,E,last,_=parse('a')
print(f(last))

# --

F,P,E,last,TEST=parse('b')
S=0
for t in TEST:
    for i,v in enumerate(t,1):
        F[i]=v
    S+=f(last)
print(S)

# --

F,P,E,last,TEST=parse('c')
max_test={}
for v in E.values():
    for x,y in v:
        if x in F:
            if x not in max_test:
                max_test[x]=set()
            max_test[x]|={int(y>0)}

MAX=0
V=[max_test.get(i,{0,1})for i in sorted(F)]
for p in product(*V):
    for i,v in enumerate(p,1):
        F[i]=v
    MAX=max(MAX,f(last))

S=0
for t in TEST:
    for i,v in enumerate(t,1):
        F[i]=v
    x=f(last)
    if x:
        S+=MAX-x
print(S)