DAY,_,_=__file__.rpartition('.')

from math import prod

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split(','))]
        r+=l

l=[0]*91
for v in r:
    for i in range(v,91,v):
        l[i]+=1
print(sum(l))

# ---

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split(','))]
        r+=l

l=[]
r=[0,*r]
for i in range(len(r)):
    v=r[i]
    if v:
        for j in range(i,len(r),i):
            r[j]-=1
        l+=i,

print(prod(l))

# ---

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split(','))]
        r+=l


l=[]
r=[0,*r]
for i in range(len(r)):
    v=r[i]
    if v:
        for j in range(i,len(r),i):
            r[j]-=1
        l+=i,


L=l
t=202520252025000

l,r=0,t
while l<r:
    m=(l+r)//2
    s=0
    for v in L:
        s+=m//v
    if s<t:
        l=m
    else:
        r=m-1
print(l)
