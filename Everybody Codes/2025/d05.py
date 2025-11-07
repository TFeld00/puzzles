DAY,_,_=__file__.rpartition('.')

import re

# ---
       
def f(r):
    i,*r=r
    x=[]
    for d in r:
        if not x:
            x+=['',d,''],
        else:
            a=1
            for v in x:
                if d>v[1] and not v[2]:
                    v[2]=d
                    a=0
                    break
                if d<v[1] and not v[0]:
                    v[0]=d
                    a=0
                    break
            if a:
                x+=['',d,''],

    s=''.join(str(v[1])for v in x)

    x=[int(''.join(str(v)for v in w))for w in x]

    return int(s),x,i

# ---


r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall(r'-?\d+',l))]
        r+=l

print(f(r)[0])

# ---

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall(r'-?\d+',l))]
        r+=l,


a = [f(v)[0] for v in r]
print(max(a)-min(a))

# ---

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall(r'-?\d+',l))]
        r+=l,
        
a = sorted(r,key=f,reverse=True)

print(sum(v*x[0]for v,x in enumerate(a,1)))
