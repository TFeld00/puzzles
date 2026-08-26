DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split('=')
        r+=[l]

*l,m=r
D={}
for a,b in l:
    D[a]=eval(b)

x,y=D['START']

d={(x,y)}
for c in m[1]:
    X,Y=D[c]
    x,y=(x+X)//2,(y+Y)//2
    d|={(x,y)}
print(len(d))

# ---

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split('=')
        r+=[l]
        
*l,m=r
D={}
for a,b in l:
    D[a]=eval(b)

x,y=D['START']

d={(x,y)}
for c in m[1]:
    X,Y=D[c]
    x,y=(x+X)//2,(y+Y)//2
    d|={(x,y)}

d2=set()
for x,y in d:
    for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
        d2|={(x+dx,y+dy)}
print(len(d2-d))

# ---

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split('=')
        r+=[l]
        
l=r
D={}
for a,b in l:
    D[a]=eval(b)

x,y=D['START']

d={(x,y)}
q=[(x,y)]
for x,y in q:
    for c in 'ABC':
        X,Y=D[c]
        x1,y1=(x+X)//2,(y+Y)//2
        if (x1,y1) not in d:
            q+=(x1,y1),
        d|={(x1,y1)}

d2=set()
for x,y in d:
    for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
        d2|={(x+dx,y+dy)}
print(len(d2-d))