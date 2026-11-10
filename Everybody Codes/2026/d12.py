DAY,_,_=__file__.rpartition('.')

from collections import Counter
from alg.floodfill import fill

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]        
        
W,H=len(r[0]),len(r)

q=[]
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='#' and (i==0 or r[i-1][j]=='.') and (j==0 or l[j-1]=='.'):
            q+=[(j,i)]

res=0
for j,i in q:
    w=h=0
    while 1:
        if j+w >= W or r[i][j+w]=='.':break
        w+=1
    while 1:
        if i+h >= H or r[i+h][j]=='.':break
        h+=1
    res+=min(w,h)
print(res)


# ---

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=list(l)
        r+=[l]
        
W,H=len(r[0]),len(r)

q=[]
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='#' and (i==0 or r[i-1][j]=='.') and (j==0 or l[j-1]=='.'):
            q+=[(j,i)]

def reflect(s):
    l=0
    while s:
        x,y=zip(*s)
        X,Y=Counter(x),Counter(y)
        a,b=X.most_common(1)[0]
        c,d=Y.most_common(1)[0]
        if b>d:
            s={(x,y)for x,y in s if x!=a}
        else:
            s={(x,y)for x,y in s if y!=c}
        l+=1
    return l

res=0
for j,i in q:
    if r[i][j]=='#':
        c,s=fill(r,(j,i),'@')
        res+=reflect(s)
        fill(r,(j,i),'.')
print(res)


# ---

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=list(l)
        r+=[l]
        
q=[]
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='#' and (i==0 or r[i-1][j]=='.') and (j==0 or l[j-1]=='.'):
            q+=[(j,i)]

def reflect(s):
    x,y=zip(*s)
    a,b=min(x),max(x)
    c,d=min(y),max(y)
    w,h=b-a+1,d-c+1
    H={(x,y)for x in range(a,b+1) for y in range(c,d+1)}-s
    if not H:
        return min(w,h)
    x,y=zip(*H)
    ha,hb=min(x),max(x)
    hc,hd=min(y),max(y)
    #V
    res1 = (ha-a) + (b-hb) + min(hb-ha+1, hc-c) + min(hb-ha+1, d-hd)
    #H
    res2 = (hc-c) + (d-hd) + min(hd-hc+1, ha-a) + min(hd-hc+1, b-hb)
    return min(res1,res2)

res=0
for j,i in q:
    if r[i][j]=='#':
        c,s=fill(r,(j,i),'@')
        res+=reflect(s)
print(res)


"""
reflect(s) example calculation

V:         H:

|||++|||   --------
|||++|||   --------
|||  |||   +++  +++
|||  |||   +++  +++
|||++|||   --------

"""