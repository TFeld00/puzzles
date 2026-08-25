DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        r+=l.rstrip('\n'),

# ---

def run():
    q=[(0,0,1)]
    seen={(0,0)}
    dist={(0,0):1}
    for x,y,s in q:
        for dx,dy in (-1,0),(1,0),(0,-1),(0,1):
            X,Y=x+dx,y+dy
            if (X,Y) not in seen and len(r[0])>X>=0<=Y<len(r):
                seen.add((X,Y))
                c=r[Y][X]
                if c=='.':
                    cost = 1
                    q+=(X,Y,s+cost),
                elif c=='*':
                    return s

print(run())

# ---

C={}
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='#':
            for y in range(i-1,i+2):
                for x in range(j-1,j+2):
                    C[(x,y)]=2

from heapq import *

def run2():
    q=[(0,0,1)]
    heapify(q)
    dist={(0,0):1}
    while q:
        x,y,s=heappop(q)
        for dx,dy in (-1,0),(1,0),(0,-1),(0,1):
            X,Y=x+dx,y+dy
            if len(r[0])>X>=0<=Y<len(r):
                c=r[Y][X]
                if c=='.':
                    cost = s+C.get((X,Y),1)
                    if cost < dist.get((X,Y),s+10):
                        dist[(X,Y)]=cost
                        heappush(q,(X,Y,cost))
                elif c=='*':
                    return s

print(run2())
