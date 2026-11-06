DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

g={}
walls=set()
for y,l in enumerate(r):
    for x,c in enumerate(l):
        if c in '<>^v':
            d='^>v<'.index(c)
            p=(x,y)
            g[p]=g.get(p,[])+[d]
        if c=='#':
            walls.add((x,y))

def run(g,rounds):
    c=0
    for i in range(rounds):
        n={}
        for (x,y) in g:
            for d in g[(x,y)]:
                dx,dy=[(0,-1),(1,0),(0,1),(-1,0)][d]
                X,Y=x+dx,y+dy
                if (X,Y) in walls:
                    X,Y,d=x,y,(d+1)%4
                    c+=1
                p=(X,Y)
                n[p]=n.get(p,[])+[d]
        for v in n:
            if len(n[v])>1:
                n[v] = [(d+2)%4 for d in n[v]]
                c+=len(n[v])
        g=n
    return c

print(run(g,10))

# ---

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

MAX = 10000
g={}
walls=set()
for y,l in enumerate(r):
    for x,c in enumerate(l):
        if c in '<>^v':
            d='^>v<'.index(c)
            p=(x,y)
            g[p]=g.get(p,[])+[(d,MAX)]
        if c=='#':
            walls.add((x,y))

def run(g):
    c=0
    i=0
    while 1:
        i+=1
        n={}
        for (x,y) in g:
            for d,col in g[(x,y)]:
                dx,dy=[(0,-1),(1,0),(0,1),(-1,0)][d]
                X,Y=x+dx,y+dy
                if (X,Y) in walls:
                    X,Y,d=x,y,(d+1)%4
                    c+=1
                    col-=1
                p=(X,Y)
                if col>0:
                    n[p]=n.get(p,[])+[(d,col)]
        for v in n:
            if len(n[v])>1:
                c+=len(n[v])
                n[v] = [((d+2)%4,col-1) for d,col in n[v]if col>1]
        g=n
        if not g:
            return i

print(run(g ))

# ---

r=[]
s=0
t=''

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

MAX = 1000000000000
g={}
walls=set()
for y,l in enumerate(r):
    for x,c in enumerate(l):
        if c in '<>^v':
            d='^>v<'.index(c)
            p=(x,y)
            g[p]=g.get(p,[])+[(d,MAX)]
        if c=='#':
            walls.add((x,y))

def move(g):
    n={}
    total=0
    for (x,y) in g:
        for d,col in g[(x,y)]:
            total+=1
            dx,dy=[(0,-1),(1,0),(0,1),(-1,0)][d]
            X,Y=x+dx,y+dy
            if (X,Y) in walls:
                X,Y,d=x,y,(d+1)%4
                col-=1
            p=(X,Y)
            if col>0:
                n[p]=n.get(p,[])+[(d,col)]
    for v in n:
        if len(n[v])>1:
            n[v] = [((d+2)%4,col-1) for d,col in n[v]if col>1]
        total-=len(n[v])
    return n,total>0

def state(A):
    l=[]
    for p,v in A:
        l+=(p,*(a for a,b in v)),
    return tuple(l)

def run2(A,B,loop):
    g={}
    M=[]
    C=[]
    for a,b in zip(A,B):
        for x,y in zip(a[1],b[1]):
            C+=(a[0],x,y[1]-x[1]),
            M+=-(x[1]//-(y[1]-x[1]))-1,
    r=min(M)
    for p,(d,c),x in C:
        g[p]=g.get(p,[]) + [(d,c-x*r)]
    return g,r*loop

def run(g):
    i=0
    init=g
    B=sorted(init.items())
    seenpos={state(B):i}
    seen={i:B}
    while 1:
        i+=1
        g,t=move(g)
        if t and PRINT_DEAD:print(i)
        A=sorted(g.items())
        curr = state(A)
        if curr in seenpos:
            j=seenpos[curr]
            loop=i-j
            B=seen[j]
            g,id=run2(A,B,loop)
            i+=id
            seenpos={}
            seen={}
        seenpos[curr]=i
        seen[i]=A

        if not g:
            return i

PRINT_DEAD = 0
print(run(g))