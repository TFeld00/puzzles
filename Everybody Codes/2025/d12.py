DAY,_,_=__file__.rpartition('.')

# ---

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
W,H=len(r[0]),len(r)
s=set()
q=[[0,0,r[0][0]]]
for i,j,c in q:
    if (i,j) in s:continue
    s|={(i,j)}
    for dx,dy in [-1,0],[1,0],[0,-1],[0,1]:
        x,y=i+dx,j+dy
        if (x,y) not in s:
            if 0<=x<W and 0<=y<H and r[y][x]<=c:
                q+=[[x,y,r[y][x]]]

print(len(s))

# ---

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
        
W,H=len(r[0]),len(r)
s=set()
q=[[0,0],[W-1,H-1]]
for i,j in q:
    if (i,j) in s:continue
    c=r[j][i]
    s|={(i,j)}
    for dx,dy in [-1,0],[1,0],[0,-1],[0,1]:
        x,y=i+dx,j+dy
        if (x,y) not in s:
            if 0<=x<W and 0<=y<H and r[y][x]<=c:
                q+=[[x,y]]

print(len(s))

# ---

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

W,H=len(r[0]),len(r)


def f(r,rem):
    t={(i,j)for i in range(W)for j in range(H)}-rem
    m=0,set()
    while t:
        (v)=max(t,key=lambda v:r[v[1]][v[0]])
        t.remove(v)
        s=set()
        
        q=[v]
        for i,j in q:
            if (i,j) in s:continue
            c=r[j][i]
            s|={(i,j)}
            for dx,dy in [-1,0],[1,0],[0,-1],[0,1]:
                x,y=i+dx,j+dy
                if (x,y) not in s:
                    if 0<=x<W and 0<=y<H and r[y][x]<=c:
                        q+=[[x,y]]
        t-=s
        w=len(s-rem)
        if w>m[0]:
            m=len(s-rem),s

    return m

_,s1=f(r,set())
_,s2=f(r,s1)
_,s3=f(r,s1|s2)

print(len(s1|s2|s3))
