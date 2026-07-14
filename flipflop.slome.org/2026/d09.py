DAY,_,_=__file__.rpartition('.')

r=[]
with open(f'{DAY}.txt', 'r') as F:
    for l in F:
        l=l.rstrip('\n')
        r+=list(l),


for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='S':
            sx,sy=j,i
        if c=='E':
            tx,ty=j,i
        
q=[(sx,sy,0)]
seen={(sx,sy)}
for x,y,m in q:
    if (x,y)==(tx,ty):
        print(m)
        break
    for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
        X,Y=x+dx,y+dy
        if r[Y][X]in'.E' and (X,Y) not in seen:
            q+=(X,Y,m+1),
            seen|={(X,Y)}
        

        
q=[(sx,sy,0)]
seen={(sx,sy)}
for x,y,m in q:
    if (x,y)==(tx,ty):
        print(m)
        break
    for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
        X,Y=x,y
        while 1:
            X,Y=X+dx,Y+dy
            if r[Y][X]not in'.E':
                X,Y=X-dx,Y-dy
                break
        if (X,Y) not in seen:
            q+=(X,Y,m+1),
            seen|={(X,Y)}
    for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
        X,Y=x+dx,y+dy
        if r[Y][X]in'.E' and (X,Y) not in seen:
            q+=(X,Y,m+1),
            seen|={(X,Y)}
        



q=[(0,sx,sy,(-1,))]
seen={(sx,sy,(-1,))}
from heapq import *
M=0
heapify(q)
while 1:
    m,x,y,p1=heappop(q)
    if (x,y)==(tx,ty):
        print(m)
        break
    for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
        X,Y=x,y
        
        while 1:
            X,Y=X+dx,Y+dy
            if r[Y][X]not in'.E':
                X,Y=X-dx,Y-dy
                break
        if p1==(x,y):
            if (X,Y,(X,Y)) not in seen:
                heappush(q,(m+2,X,Y,(X,Y)))
                seen|={(X,Y,(X,Y))}
        elif (X,Y)==(x,y) and (x,y,(X,Y)) not in seen:
            heappush(q,(m+1,x,y,(X,Y)))
            seen|={(x,y,(X,Y))}
    
    for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
        X,Y=x+dx,y+dy
        if r[Y][X]in'.E' and (X,Y,p1) not in seen:
            heappush(q,(m+1,X,Y,p1))
            seen|={(X,Y,p1)}
