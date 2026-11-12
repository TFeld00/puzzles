DAY,_,_=__file__.rpartition('.')

from itertools import *
import networkx as nx

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]        
        
W,H=len(r[0]),len(r)

s=W
for i,l in enumerate(r):
    s+=1
    for j,c in enumerate(l):
        if i<H-1:
            s+=c!=r[i+1][j]
        else:
            s+=1
        if j<W-1:
            s+=c!=l[j+1]
        else:
            s+=1
print(s)

# ---

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
W,H=len(r[0]),len(r)

E={}
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if i in [0,H-1]:
            x=(c,'')
            E[x]=E.get(x,0)+1
        if j in [0,W-1]:
            x=(c,'')
            E[x]=E.get(x,0)+1
        if i<H-1:
            d=r[i+1][j]
            if c!=d:
                x=tuple(sorted((c,d)))
                E[x]=E.get(x,0)+1
        if j<W-1:
            d=l[j+1]
            if c!=d:
                x=tuple(sorted((c,d)))
                E[x]=E.get(x,0)+1
        
W = {}
for (a,b),v in E.items():
    W[a] = W.get(a,{})
    W[b] = W.get(b,{})
    W[a][b]=v
    W[b][a]=v

edges = [(a,b,{'weight':v})for (a,b),v in E.items()]

G=nx.Graph()
G.add_edges_from(edges)
T=nx.minimum_spanning_tree(G)
s=0
for a,b in T.edges():
    s+=W[a][b]
print(s)


# ---

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
W,H=len(r[0]),len(r)

E={}
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if i in [0,H-1]:
            x=(c,'')
            E[x]=E.get(x,0)+1
        if j in [0,W-1]:
            x=(c,'')
            E[x]=E.get(x,0)+1
        if i<H-1:
            d=r[i+1][j]
            if c!=d:
                x=tuple(sorted((c,d)))
                E[x]=E.get(x,0)+1
        if j<W-1:
            d=l[j+1]
            if c!=d:
                x=tuple(sorted((c,d)))
                E[x]=E.get(x,0)+1

ALL=set(c for l in r for c in l)

def solve(X,Y):
    W = {}
    for (a,b),v in E.items():
        W[a] = W.get(a,{})
        W[b] = W.get(b,{})
        W[a][b]=v
        W[b][a]=v
    for d in W[X]:W[X][d]=W[d][X]=0
    for d in W[Y]:W[Y][d]=W[d][Y]=0
    W[X][Y]=0
    W[Y][X]=0

    edges = [(a,b,{'weight':W[a][b]})for (a,b),v in E.items()]
    edges+=[(X,Y,{'weight':0})]

    G=nx.Graph()
    G.add_edges_from(edges)
    T=nx.minimum_spanning_tree(G)
    s=0
    for a,b in T.edges():
        s+=W[a][b]
    return s


print(min(solve(X,Y) for X,Y in combinations(ALL,r=2)))