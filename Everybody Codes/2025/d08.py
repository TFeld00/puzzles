DAY,_,_=__file__.rpartition('.')


r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(',')
        l=[*map(int,l)]
        r+=l

s=0
L=32
for i,j in zip(r,r[1:]):
    if (j-i)%L==L//2:s+=1
print(s)


# ---

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(',')
        l=[*map(int,l)]
        r+=l

s=0
l=[]
for i,j in zip(r,r[1:]):
    l+=sorted([i,j]),

L=256
for i,(a,b) in enumerate(l):
    for x,y in l[i+1:]:
        if 0<(x-a)%L<(b-a)%L<(y-a)%L:s+=1
        elif 0<(a-x)%L<(y-x)%L<(b-x)%L:s+=1
        
print(s)

# ---

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(',')
        l=[*map(int,l)]
        r+=l

s=0
l=[]
for i,j in zip(r,r[1:]):
    l+=sorted([i,j]),

L=256
R=0
for a in range(1,1+L):
    print(end='.')
    for b in range(a+1,1+L):
        s=0
        for x,y in l:
            if 0<(x-a)%L<(b-a)%L<(y-a)%L:s+=1
            elif 0<(a-x)%L<(y-x)%L<(b-x)%L:s+=1
            elif (x,y)==(a,b):s+=1
        R=max(R,s)

print()
print(R)
