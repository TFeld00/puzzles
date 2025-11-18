DAY,_,_=__file__.rpartition('.')


r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]        
        
W=len(r)
s=0
for _ in range(1,11):
    x=0
    if not s:
        for i in range(W-1):
            j=i+1
            if r[i]>r[j]:
                r[i]-=1
                r[j]+=1
                x=1
    if not x:
        for i in range(W-1):
            j=i+1
            if r[j]>r[i]:
                r[j]-=1
                r[i]+=1
                x=1
        s=1
        
print(sum(i*x for i,x in enumerate(r,1)))


# ---

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]
        
W=len(r)
s=0
I=0
while len(set(r))>1:
    I+=1
    x=0
    if not s:
        for i in range(W-1):
            j=i+1
            if r[i]>r[j]:
                r[i]-=1
                r[j]+=1
                x=1
    if not x:
#        if not s:
#            print(I,r)
        for i in range(W-1):
            j=i+1
            if r[j]>r[i]:
                r[j]-=1
                r[i]+=1
                x=1
        s=1

print(I)


# ---

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]
    
A=sum(r)//len(r)

c=0
for i,v in enumerate(r):
    if v>A:
        break
for i,v in enumerate(r):
    if v<A:
        c+=(A-v)

print(c)
