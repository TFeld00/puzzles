DAY,_,_=__file__.rpartition('.')

r=[]
with open(f'{DAY}.txt', 'r') as F:
    for l in F:
        l=l.rstrip('\n')
        r+=list(l),

bt={}
sx=sy=0
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='S':
            sx,sy=j,i
        if c.isupper():
            bt[c]=(j,i)

# ---

seen={(sx,sy)}
q=[(sx,sy,1)]
lights=[]
for x,y,d in q:
    for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
        X,Y=x+dx,y+dy
        if len(r)>Y>=0<=X<len(r[0]):
                c=r[Y][X]
                if (X,Y) not in seen:
                    seen|={(X,Y)}
                    if c=='#':
                        q+=(X,Y,1-d),
                    elif c=='*':
                        lights+=(Y,X,1-d),

res=0
for y,x,v in sorted(lights):
    res*=2
    res+=v
print(res)

# ---


m=[[' 'for c in l]for l in r]

seen={(sx,sy)}
q=[(sx,sy,1,0)]
lights=[]
for x,y,d,b in q:
    m[y][x]='LR'[d]
    for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
        X,Y=x+dx,y+dy
        if len(r)>Y>=0<=X<len(r[0]):
                c=r[Y][X]
                if (X,Y) not in seen:
                    if c in '#3':
                        seen|={(X,Y)}
                        q+=(X,Y,1-d,0),
                    elif c=='*' and not b:
                        seen|={(X,Y)}
                        lights+=(Y,X,1-d),
                    elif c.isalpha() and c.islower():
                        x1,y1=bt[c.upper()]
                        seen|={(x1,y1)}
                        q+=(x1,y1,d,1),


res=0
for y,x,v in sorted(lights):
    res*=2
    res+=v
    m[y][x]='.*'[v]
print(res)

# ---

m=[[' 'for c in l]for l in r]

seen={(sx,sy)}
q=[(sx,sy,1,0,'S')]
gr={}
tr={}
lights=[]
for x,y,d,b,g in q:
    m[y][x]='<>'[d]
    if r[y][x].isupper():
        m[y][x]=r[y][x]
    for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
        X,Y=x+dx,y+dy
        if len(r)>Y>=0<=X<len(r[0]):
                c=r[Y][X]
                if (X,Y) not in seen:
                    if c in '#3':
                        seen|={(X,Y)}
                        gr[g]=gr.get(g,0)+1
                        q+=(X,Y,1-d,0,g),
                    elif c=='*' and not b:
                        seen|={(X,Y)}
                        lights+=(Y,X,1-d,g),
                        m[Y][X]=','
                    elif c.isalpha() and c.islower():
                        m[Y][X]=c
                        x1,y1=bt[c.upper()]
                        seen|={(x1,y1)}
                        tr[g]=tr.get(g,set())|{c.upper()}
                        q+=(x1,y1,d,1,c.upper()),

def prime(v):
    if v<2:return 0
    for i in range(2,v):
        if v%i==0:return 0
    return 1

res=0
ll=lights
lights=[]
r={v:v=='S' or not prime(gr[v])for v in gr}

q=['S']
for v in q:
    for w in tr.get(v,[]):
        if not r[v]:
            r[w]=0
        q+=[w]

for w in ll:
    if r[w[3]] or w[3]=='S':
        lights+=w,

for y,x,v,_ in sorted(lights):
    res*=2
    res+=v
    m[y][x]='.*'[v]
print(res)

#with open(f'{DAY}.o.txt', 'w') as F:
#    for l in m:F.write(''.join(l)+'\n')
