DAY,_,_=__file__.rpartition('.')

from img.img import write_img_fromlist
from alg.cellular import to_lists
from queue import *


r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(',')
        r+=l
        

d={(0,0):1}
x=y=0
dx,dy=1,0
L=[(-1,0),(0,1),(1,0),(0,-1)]
for v in r:
    if v[0]=='R':
        dx,dy = L[(L.index((dx,dy))+1)%4]
    else:
        dx,dy = L[(L.index((dx,dy))-1)%4]
    q=int(v[1:])
    for i in range(q):
        x+=dx
        y+=dy
        d[(x,y)]=1

E=(x,y)



def bfs(r,x,y):
    
    q=Queue()
    s=set()
    q.put((x,y,0))
    while not q.empty():
        x,y,l=q.get()
        
        if (x,y)==E:
            print(l)
            #WIN
            return l
        
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            X,Y=x+dx,y+dy
            if (X,Y)in s:continue

            s|={(X,Y)}
            if (X,Y) not in r or (X,Y)==E:
                q.put((X,Y,l+1))

bfs(d,0,0)

# ---


r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(',')
        r+=l

d={(0,0):1}
x=y=0
dx,dy=1,0
L=[(-1,0),(0,1),(1,0),(0,-1)]
e=[]
for v in r:
    if v[0]=='R':
        dx,dy = L[(L.index((dx,dy))+1)%4]
    else:
        dx,dy = L[(L.index((dx,dy))-1)%4]
    q=int(v[1:])
    for i in range(q):
        x+=dx
        y-=dy
        d[(x,y)]=1

    e+=[(x,y)]

E=(x,y)


bfs(d,0,0)

## P 2, 'manual' path

x,y=0,0

L=[(-1,0),(0,1),(1,0),(0,-1)]
R=0
for dd,v in [[1,1],[4,2],[3,3],[2,4],[1,9],[4,16],[3,25],[2,28],[1,37],[4,46],[3,61],[1,145],[3,77],[2,86],[1,99],[4,190],[1,190]]:
    if dd==1:dd=3
    elif dd==3:dd=1
    dx,dy=L[dd%4]
    X,Y=e[v-1]
    if dx:
       
        w=abs(x-X)+1
        x=X+dx
    else:
        w=abs(y-Y)+1
        y=Y+dy

    R+=w

print(R)


#

L=to_lists(d)

COLS = {
    0: (255, 255, 255),
    1: (0, 0, 0),
}

write_img_fromlist(L,DAY+"b",COLS)


# P3 'manual' path


r=[]
s=0
t=''

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(',')
        r+=l

e=[]

x=y=0
dx,dy=1,0
L=[(-1,0),(0,1),(1,0),(0,-1)]
qq=[]
for v in r:
    if v[0]=='R':
        dx,dy = L[(L.index((dx,dy))+1)%4]
    else:
        dx,dy = L[(L.index((dx,dy))-1)%4]
    q=int(v[1:])
    qq+=q,
    X=x+dx*q
    Y=y+dy*q
    

    e+=[((x,y),(X,Y))]
    x,y=X,Y

E=x,y

x,y=0,0

L=[(-1,0),(0,1),(1,0),(0,-1)]
R=0
PATH = [[1,1],[4,4],[3,7],[2,10],[1,15],[4,28],[3,37],[2,56],[1,67],[4,80],[3,85],[1,173],[3,95],[2,104],[4,206],[2,112],[1,240],[4,240]]
for dd,v in PATH:
    dx,dy=L[dd%4]
    X,Y=e[v-1][1]
    if dx:
        w=abs(x-X)+1
        x=X+dx
    else:
        w=abs(y-Y)+1
        y=Y+dy
    R+=w+1

print(R-2)


PATH2 = [i for _,i in PATH]
d={(0,0):1}
for I,((x,y),(X,Y)) in enumerate(e,1):
    if x>X:x,X=X,x
    if y>Y:y,Y=Y,y
    M=50000
    x//=M
    X//=M
    y//=M
    Y//=M
    for i in range(x,X+1):
        for j in range(y,Y+1):
            d[(i,j)]=2 if I in PATH2 else 1

x, y = zip(*d.keys())
d[(min(x)-5,min(y)-5)]=0
d[(max(x)+5,max(y)+5)]=0
L=to_lists(d)

COLS = {
    0: (255, 255, 255),
    1: (0, 0, 0),
    1: (255, 0, 0),
}

write_img_fromlist(L,DAY+'c',COLS)
