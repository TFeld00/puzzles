DAY,_,_=__file__.rpartition('.')

import re

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.translate(str.maketrans('rRgGbB','010101'))
        l=[re.findall(r'\w+',l)]
        r+=l
s=0
for x,R,g,b in r: 
    R=int(R,2)
    g=int(g,2)
    b=int(b,2)
    if b<g>R:
        s+=int(x)
print(s)

### -------------------

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.translate(str.maketrans('rRgGbBsS','01010101'))
        l=[re.findall(r'\w+',l)]
        r+=l

r2={}
for x,R,g,b,s in r: 
    R=int(R,2)
    g=int(g,2)
    b=int(b,2)
    s=int(s,2)
    if s not in r2:
        r2[s]=[]
    r2[s]+=[[x,R+g+b]]
v=max(r2)
print(int(min(r2[v],key=lambda x:x[1])[0]))

### -------------------

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.translate(str.maketrans('rRgGbBsS','01010101'))
        l=[re.findall(r'\w+',l)]
        r+=l
r2=[[]for _ in ' '*6]
for x,R,g,b,s in r: 
    R=int(R,2)
    g=int(g,2)
    b=int(b,2)
    s=int(s,2)
    i=0
    if s<=30:i=0
    elif s>=33:i=1
    else:continue
    if g<R>b:i+=0
    elif R<g>b:i+=2
    elif R<b>g:i+=4
    else:continue
    r2[i]+=[int(x)]

v=max(r2,key=len)
print(sum(v))