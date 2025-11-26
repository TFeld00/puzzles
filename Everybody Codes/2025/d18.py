DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
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
ALL={}
for v in E.values():
    for x,y in v:
        if x not in ALL:
            ALL[x]=[]
        ALL[x]+=y,

for v,w in ALL.items():
    if v in F:
        if sum(w)<=0:
            F[v]=0
        else:
            F[v]=1

MAX=f(last)

S=0
for t in TEST:
    for i,v in enumerate(t,1):
        F[i]=v
    x=f(last)
    if x:
        S+=MAX-x
print(S)