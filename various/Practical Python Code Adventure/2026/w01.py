DAY,_,_=__file__.rpartition('.')
import re


r=[]
with open(f'{DAY}.1.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=l,

T=str.maketrans(r[1],r[0])

r=r[3:]
s=''
d=1
for l in r:
    l=l.translate(T)
    s+=l[::d]
    d=-d

w=set()
l={x for x in re.findall(r'\w+',s) if len(x) == 5}
w|=l

print(s)
print(sorted(w)[19])
print()

# ---


r=[]
with open(f'{DAY}.2.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=l,

T1=str.maketrans(r[1],r[0])
T2=str.maketrans(r[2],r[0])
T3=str.maketrans(r[3],r[0])

m=r[5:]
s=''
seen=set()
dx,dy=1,0
x=y=0
while 0<=x<len(m[0])and 0<=y<len(m) and (x,y) not in seen:
    seen|={(x,y)}
    c=m[y][x]
    if c in r[0]:
        dx,dy=1,0
    elif c in r[1]:
        dx,dy=0,1
        c=c.translate(T1)
    elif c in r[2]:
        dx,dy=0,-1
        c=c.translate(T2)
    elif c in r[3]:
        dx,dy=-1,0
        c=c.translate(T3)
    s+=c
    x,y=x+dx,y+dy

print(s)
print()
