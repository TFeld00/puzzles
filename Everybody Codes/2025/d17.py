DAY,_,_=__file__.rpartition('.')

from itertools import *
from collections import defaultdict
from math import ceil
import heapq #heapq.nsmallest

r=[]
x=y=0

with open(f'{DAY}a.txt','r')as F:
    for i,l in enumerate(F):
        l=l.rstrip('\n')
        r+=[l]
        
        if '@'in l:
            x,y=l.find('@'),i


R=10
s=0        
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if (i-y)**2+(j-x)**2<=R*R:
            if c=='@':continue
            s+=int(c)
print(s)


##  --- 


r=[]
x=y=0

with open(f'{DAY}b.txt','r')as F:
    for i,l in enumerate(F):
        l=l.rstrip('\n')
        r+=[l]
        
        if '@'in l:
            x,y=l.find('@'),i


S=[]
d={}
for i,l in enumerate(r):
    for j,c in enumerate(l):
        v=ceil(((i-y)**2+(j-x)**2)**0.5)
        if c=='@':continue
        if v not in d:
            d[v]=0
        d[v]+=int(c)

a,b=max(d.items(),key=lambda v:v[1])
print(a*b)


##  --- 



r=[]
xa=ya=0
xs=ys=0

with open(f'{DAY}c.txt','r')as F:
    for i,l in enumerate(F):
        l=l.rstrip('\n')
        r+=[l]
        
        if '@'in l:
            xa,ya=l.find('@'),i
        if 'S'in l:
            xs,ys=l.find('S'),i


W,H=len(r[0]),len(r)


def dijkstra(r,init,targets,deadline):
    distances = defaultdict(lambda:defaultdict(lambda: 1e99))
    q=[]
    for v in init:
        distances[v][v]=0
        heapq.heappush(q, (0, v,v))
    while q:
        d,(x,y),o = heapq.heappop(q)
        if d > distances[o][(x,y)] or d>=deadline*30:
            continue
        if (x,y) in targets:
            continue
        for dx,dy in (-1,0),(1,0),(0,-1),(0,1):
            X,Y=x+dx,y+dy
            if 0<=X<W and 0<=Y<H:
                c=r[Y][X]
                if c=='S' or c.isdigit():
                    D=d+int(c if c!='S' else 0)
                    if D<distances[o][(X,Y)]:
                        distances[o][(X,Y)]=D
                        heapq.heappush(q, (D, (X,Y),o))
    return {o:{v:d for v,d in distances[o].items() if v in targets}for o in distances}

def value(dists):
    a,b,c,d=dists
    v=None
    for _,d1 in a.items():
        for k1,v1 in d1.items():
            if k1 in b:
                for k2,v2 in b[k1].items():
                    if k2 in c:
                        for k3,v3 in c[k2].items():
                            if k3 in d:
                                for k4,v4 in d[k3].items():
                                    if k4 == (xs,ys):
                                        w=v1+v2+v3+v4
                                        if v is None:v=w
                                        else:v = min(v,w)
    if v is not None: return v


COLS = {
    '.': (255, 0, 0),
    '#': (0, 0, 0),
}
for i in range(11):
        COLS['%X'%(i)] = (255-25*i,255-25*i,255-25*i)
        COLS[i] = (255-25*i,255-25*i,255-25*i)



gates = {(xs,ys)},{(i,ya)for i in range(xa)},{(xa,i)for i in range(ya+1,H)},{(i,ya)for i in range(xa+1,W)}

rinit=r
def loop(t):
    r1 = [list(l) for l in rinit]
    for i,l in enumerate(r):
        for j,c in enumerate(l):
            v=(((i-ya)**2+(j-xa)**2)**0.5)
            if v<=t:
                r1[i][j]='.'

    #write_img_fromlist(r1,f"{DAY}_{t}",COLS)
    dists=[]
    for a,b in pairwise(gates+gates[:1]):
        dists+=dijkstra(r1,a,b,t),
    if not all(dists):
        return
    v= value(dists)
    return v

L,R=0,len(r)

prev=1e9
for M in range(1,R):
    l=loop(M)
    if l and l<30*M+30 and l<prev:
        prev=l
        break
    print(M,30*M+30,l,prev,prev*M)
print(M,30*M+30,l,prev,prev*M)


"""  # binary search doesn't quite work..
prev=1e9
while L<R:
    M=(L+R+1)//2
    l=loop(M)
    print(L,R,M,30*M+30,l,l and l<30*M+30,prev)
    if l:
        if l<30*M+30 and l<prev:
            prev=l
            R=R-1
        else:
            L=M
    else:
        R=M-1
print(L,R,l,prev)"""
print(prev*M)