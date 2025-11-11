DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
from functools import cache

# ---

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

a,b=parse_no_headers(r)
a=a[0].split(',')

d={}
for s in b:
    x,_,y=s.split()
    y=y.split(',')
    d[x]=y

for w in a:
    if all(x in d and y in d[x] for x,y in zip(w,w[1:])):
        print(w)

# ---

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

a,b=parse_no_headers(r)
a=a[0].split(',')

d={}
for s in b:
    x,_,y=s.split()
    y=y.split(',')
    d[x]=y

r=0
for i,w in enumerate(a,1):
    if all(x in d and y in d[x] for x,y in zip(w,w[1:])):
        r+=i
print(r)

# ---

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

a,b=parse_no_headers(r)
a=a[0].split(',')

d={}
for s in b:
    x,_,y=s.split()
    y=y.split(',')
    d[x]=y

@cache
def f(w,l):
    if l==0:
        return {w}
    c=w[-1]
    if c in d:
        return {w+x for y in d[c] for x in f(y,l-1)}
    return set()

r=[]
for w in a:
    if all(x in d and y in d[x] for x,y in zip(w,w[1:])):
        l=len(w)
        for i in range(7,12):
            r+=f(w,i-l)


print(len(set(r)))