DAY,_,_=__file__.rpartition('.')

from itertools import pairwise
from collections import defaultdict

## ---

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

s=0
for l in r:
    for a,b in pairwise(l):
        s+=a==b=='T'
i=1
for a,b in pairwise(r):
    for x,y in zip(a[i::2],b[i::2]):
        s+=x==y=='T'
    i^=1
print(s)

## ---

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

e=defaultdict(lambda:[])
s=0
for i,l in enumerate(r):
    for x,a in enumerate(l):
        if a=='S':
            xs,ys=i,x
        if a=='E':
            xe,ye=i,x

for i,l in enumerate(r):
    for x,y in pairwise(range(len(l))):
        a,b=l[x],l[y]
        if a in 'SET' and b in 'SET':
            a,b=(i,x),(i,y)
            e[a]+=b,
            e[b]+=a,
            
i=1
for j,k in pairwise(range(len(r))):
    A,B=r[j],r[k]
    for q in range(i,len(A),2):
        a,b=A[q],B[q]
        if a in 'SET' and b in 'SET':
            a,b=(j,q),(k,q)
            e[a]+=b,
            e[b]+=a,
    i^=1


q=[[xs,ys,0]]
s=set()
for x,y,m in q:
    if (x,y) in s:
        continue
    if (x,y)==(xe,ye):
        print(m)
        break
    s|={(x,y)}
    for X,Y in e[(x,y)]:
        if (X,Y) not in s:
            q+=[X,Y,m+1],



## ---
r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
                
W,H=len(r[0]),len(r)

def trans(x,y):
    return H-(y+x)//2-1-(y+x)%2,(W-y)//2-(y*x)%2+x+-~x//2

e=defaultdict(lambda:[])
for i in range(H):
    for j in range(W):
        x=r[i][j]
        if x=='S':
            xs,ys=i,j
        if x=='E':
            xe,ye=i,j
        if x in 'SET':
            moves = [(0,-1),(0,1),(0,0)]
            if i%2==j%2:moves += (-1,0),
            else: moves += (1,0),
            for dx,dy in moves:
                X,Y=i+dx,j+dy
                if 0<=X<len(r) and 0<=Y<len(r[0]) and r[X][Y]!='.':
                    X,Y=trans(X,Y)
                    y=r[X][Y]
                    if y in 'SET':
                        e[(i,j)]+=(X,Y),

def draw(x,y,m):
    for i in range(H):
        S=' '*i
        for j in range(W):
            c=r[i][j]
            X,Y=i,j
            if c!='.':
                for _ in range(m%3):
                    X,Y=trans(X,Y)
                S+='.'if (i,j)==(x,y) else r[X][Y]
        print(S)

q=[[xs,ys,0]]
s=set()
for x,y,m in q:
    if (x,y) in s:
        continue
    if (x,y)==(xe,ye):
        print(m)
        break
    s|={(x,y)}
    for X,Y in e[(x,y)]:
        if (X,Y) not in s:
            q+=[X,Y,m+1],

