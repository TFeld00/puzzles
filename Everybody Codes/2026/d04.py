DAY,_,_=__file__.rpartition('.')


r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        d=[]
        for a in l:
            x,y=a.split('=')
            d+=int(y),
        r+=[d]

d=[0]*len({x[0]for x in r})
for i,q,p,t in r:
    d[i-1]+=t
print(sum(a*b for a,b in enumerate(sorted(d),1)))


# ---

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        d=[]
        for a in l:
            x,y=a.split('=')
            d+=int(y),
        r+=[d]

d=[[0,0]for _ in range(len({x[0]for x in r}))]
for i,q,p,t in r:
    d[i-1][1]+=t
    d[i-1][0]-=1

print(sum(a*b[1] for a,b in enumerate(sorted(d),1)))


# ---

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        d=[]
        for a in l:
            x,y=a.split('=')
            d+=int(y),
        r+=[d]

d=[0 for _ in range(len({x[0]for x in r}))]

Q={}
for i,q,p,t in r:
    Q[(q,p)]=Q.get((q,p),[]) + [(t,i)]

T=[0]*len(d)
for (q,p),v in sorted(Q.items()):
    if p==1:
        T=[0]*len(d)
    for t,i in v:
        T[i-1]+=t
    s=p*50
    prev=-1
    s2=s
    x=[(T[i-1],i) for t,i in v]
    for t,i in sorted(x):
        if t!=prev:
            s=s2
            if s<0:break
        d[i-1]+=s
        s2-=1
        prev=t

s=0
x=1
prev=-1
x2=x
for v in sorted(d,reverse=True):
    if v!=prev:
        x=x2
    prev=v
    s+=x*v
    x2+=1
print(s)