DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split('-')[1].split()
        r+=[l]
        
s=0
for a,b in r:
    p=len(b)-1
    for x,y in zip(a,b):
        
        s+=int(y)*int(x)**p
        p-=1
print(s)


# ---

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split('-')[1].split()
        r+=[l]
        
s=0
for a,b in r:
    p=len(b)
    a=(a*p)[-p:]
    q=0
    p-=1
    for x,y in zip(a,b):
        q+=int(y)*int(x)**p
        p-=1
    s+=q
print(s)


# ---

r=[]
with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split('-')[1].split()
        r+=[l]


def iso(a,b):
    b=str(b)
    p=len(b)
    a=(a*p)[-p:]
    q=0
    p-=1
    for x,y in zip(a,b):
        q+=int(y)*int(x)**p
        p-=1
    return q

s=0
for a,b in r:
    q=iso(a,b)
    for b2 in range(q,int(b)):
        q2=iso(a,b2)
        if q2==q:
            q=0
            break
    s+=q
print(s)
