DAY,_,_=__file__.rpartition('.')


r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='#':
            cx,cy=j,i
        elif c=='@':
            vx,vy=j,i

s={(vx,vy)}
t=0
mi=0
while 1:
    dy,dx=[[-1,0],[0,1],[1,0],[0,-1]][mi%4]
    mi+=1
    x,y=vx+dx,vy+dy
    if (x,y) not in s:
        vx,vy=x,y
        t+=1
        s|={(x,y)}
    if (x,y)==(cx,cy):break
print(t)


### --------------

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='#':
            cx,cy=j,i
        elif c=='@':
            vx,vy=j,i

s={(vx,vy),(cx,cy)}

def fill(s):
    X,Y=zip(*s)
    a,b=min(X)-1,max(X)+1
    A,B=min(Y)-1,max(Y)+1
    seen=set((a,A))
    q=[(a,A)]
    for x,y in q:
        for dx,dy in [-1,0],[1,0],[0,-1],[0,1]:
            X,Y=x+dx,y+dy
            if a<=X<=b and A<=Y<=B:
                if (X,Y) not in seen and (X,Y)not in s:
                    seen|={(X,Y)}
                    q.append((X,Y))
    for i in range(a,b):
        for j in range(A,B):
            if (i,j) not in seen:
                s.add((i,j))

t=0
mi=0
while 1:
    dy,dx=[[-1,0],[0,1],[1,0],[0,-1]][mi%4]
    mi+=1
    x,y=vx+dx,vy+dy
    if (x,y) not in s:
        vx,vy=x,y
        t+=1
        s|={(x,y)}
        fill(s)
    if (cx-1,cy) in s and (cx+1,cy) in s and (cx,cy-1) in s and (cx,cy+1) in s:break
print(t)


### --------------


r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

C=[]

for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='#':
            C+=[(j,i)]
        elif c=='@':
            vx,vy=j,i

s={(vx,vy),*C}

def fill(s):
    X,Y=zip(*s)
    a,b=min(X)-1,max(X)+1
    A,B=min(Y)-1,max(Y)+1
    seen=set((a,A))
    q=[(a,A)]
    for x,y in q:
        for dx,dy in [-1,0],[1,0],[0,-1],[0,1]:
            X,Y=x+dx,y+dy
            if a<=X<=b and A<=Y<=B:
                if (X,Y) not in seen and (X,Y)not in s:
                    seen|={(X,Y)}
                    q.append((X,Y))
    for i in range(a,b):
        for j in range(A,B):
            if (i,j) not in seen:
                s.add((i,j))

t=0
mi=0
while 1:
    dy,dx=[[-1,0],[-1,0],[-1,0],[0,1],[0,1],[0,1],[1,0],[1,0],[1,0],[0,-1],[0,-1],[0,-1]][mi%12]
    mi+=1
    x,y=vx+dx,vy+dy
    if (x,y) not in s:
        vx,vy=x,y
        t+=1
        s|={(x,y)}
        fill(s)
    if all((cx-1,cy) in s and (cx+1,cy) in s and (cx,cy-1) in s and (cx,cy+1) in s for cx,cy in C):break
print(t)
