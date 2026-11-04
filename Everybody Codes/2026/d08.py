DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[int(v) if v.isdigit() else 0 for v in l]
        r+=[l]

W,H=len(r[0]),len(r)

q=[]
for i in range(W):
    q+=(0,i),
for i in range(H):
    q+=(i,0),
q=list(set(q))
s=0

for y,x in q:
    sh=0
    while 1:
        v=r[y][x]
        if v>sh:
            sh=v
            s+=1
        x,y=x+1,y+1
        sh=max(0,sh-1)
        if x>=W or y>=H:break

print(s)


# -----

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[int(v) if v.isdigit() else 0 for v in l]
        r+=[l]
        
W,H=len(r[0]),len(r)

def f(I,Iy,J,Jx,dx,dy,ox=lambda i:0):
    q=[]
    for i in range(I):
        q+=(Iy,i),
    for i in range(J):
        q+=(i,Jx + ox(i)),

    s=0
    for y,x in q:
        sh=0
        while 0<=x<W and 0<=y<H:
            v=r[y][x]
            if v>sh:
                sh=v
                s+=1
            x,y=x+dx,y+dy
            sh=max(0,sh-1)
    return s

res=[]
res+=f(W,0,H,0,1,1),
res+=f(W,0,H,W-1,-1,1),
res+=f(0,0,H,W-1,-2,0,lambda i:(H//2+i)%-2),
res+=f(W,H-1,H,W-1,-1,-1),
res+=f(W,H-1,H,0,1,-1),
res+=f(0,0,H,0,2,0,lambda i:(H//2+i)%2),

print(sum(res))

# ---

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[int(v) if v.isdigit() else 0 for v in l]
        r+=[l]
        
W,H=len(r[0]),len(r)

def f(I,Iy,J,Jx,dx,dy,ox=lambda i:0):

    q=[]
    for i in range(I):
        q+=(Iy,i),
    for i in range(J):
        q+=(i,Jx + ox(i)),
    q=list(set(q))

    s=0
    new_ents=0
    for y,x in q:
        sh=0
        while 0<=x<W and 0<=y<H:
            v=r[y][x]
            if v<0:
                v+=1
                if v==0:v=1
                r[y][x]=v
            elif v>sh:
                sh=v
                s+=1
                r[y][x]+=1
                if r[y][x]>9:
                    new_ents += 1
                    r[y][x]=-3
            x,y=x+dx,y+dy
            sh=max(0,sh-1)

    return new_ents, s

MOVES=[(W,0,H,0,1,1),
(W,0,H,W-1,-1,1),
(0,0,H,W-1,-2,0,lambda i:(H//2+i)%-2),
(W,H-1,H,W-1,-1,-1),
(W,H-1,H,0,1,-1),
(0,0,H,0,2,0,lambda i:(H//2+i)%2)]

total=0
ents =0
rounds=0
while ents <100000:
    a,b=f(*MOVES[rounds%6])
    rounds+=1
    ents+=a
    total+=b
print(total)