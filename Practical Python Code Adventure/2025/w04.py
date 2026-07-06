DAY,_,_=__file__.rpartition('.')

import re

r=[]
with open(f'{DAY}.1.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[*map(int,re.findall(r'\d+',l))],

x,y='',''
for l in r:
    m1,x1,y1,m2,x2,y2,m3,x3,y3=l
    v=(m1*x1+m2*x2+m3*x3)//(m1+m2+m3)
    x+=chr(v)
    w=(m1*y1+m2*y2+m3*y3)//(m1+m2+m3)
    y+=chr(w)
print(x,y)

# ---

r=[]
with open(f'{DAY}.2.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[*map(int,l.split(','))],

w,h=len(r[0]),len(r)
C=[]
a=[(x,y)for y in range(h) for x in range(w)if r[y][x]]
s=set()

while a:
    x,y=a.pop()
    if not r[y][x]:continue
    q=[(x,y,r[y][x])]
    c=[]
    r[y][x]=0
    for x,y,v in q:
        c+=(x,y,v),
        for dx,dy in (-1,0),(1,0),(0,-1),(0,1):
            X,Y=x+dx,y+dy
            if h>Y>=0<=X<w and r[Y][X]:
                q+=(X,Y,r[Y][X]),
                r[Y][X]=0
    m=sum(v for x,y,v in c)
    cx=sum(x*v for x,y,v in c)//m
    cy=sum(y*v for x,y,v in c)//m
    C+=(m,','.join([str(cx),str(cy)])),
print(max(C)[1])


