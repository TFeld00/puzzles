DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(',')
        r+=[l]

a,_,b=r

i=0
for m in b:
    n=int(m[1:])
    d = -1 if 'L'in m else 1
    i+=d*n
    if i<0:i=0
    if i>=len(a):i=len(a)-1
print(a[i])

#---

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(',')
        r+=[l]

a,_,b=r

i=0
for m in b:
    n=int(m[1:])
    d = -1 if 'L'in m else 1
    i+=d*n
print(a[i%len(a)])

#---

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(',')
        r+=[l]
        

a,_,b=r

i=0
for m in b:
    n=int(m[1:])
    d = -1 if 'L'in m else 1
    j=(d*n)%len(a)
    a[i],a[j]=a[j],a[i]
print(a[0])