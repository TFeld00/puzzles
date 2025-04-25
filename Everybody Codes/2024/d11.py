DAY,_,_=__file__.rpartition('.')

from collections import *
import re

def run(v,d,steps):
    s=Counter([v])
    for i in range(steps):
        c=Counter()
        for x,v in s.items():
            c+={q:w*v for q,w in d[x].items()}
        s=c
    return sum(s.values())

## Part 1 ##
d={}
with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,*b=re.split(r'\W',l)
        d[a]=Counter(b)

print(run('A',d,4))

## Part 2 ##
d={}
with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,*b=re.split(r'\W',l)
        d[a]=Counter(b)

print(run('Z',d,10))

## Part 3 ##
d={}
with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,*b=re.split(r'\W',l)
        d[a]=Counter(b)
l=[]
for v in d:
    l+=run(v,d,20),

print(max(l)-min(l))