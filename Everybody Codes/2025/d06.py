DAY,_,_=__file__.rpartition('.')

# ---

s=''

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=l
        
r=0
for i,c in enumerate(s):
    if c=='a':
        for x in s[:i]:
            if x=='A':
                r+=1
print(r)

# ---

s=''

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=l
        
r=0
for a,A in 'aA','bB','cC':
    for i,c in enumerate(s):
        if c==a:
            for x in s[:i]:
                if x==A:
                    r+=1
print(r)

# ---


s=''

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=l

r=0
w=1000
n=1000
l=len(s)
for a,A in 'aA','bB','cC':
    for i,c in enumerate(s):
        if c==a:
            for j in range(i-w,i+w+1):
                x=s[j%l]
                if x==A:
                    r+=n - (j<0 or j>=l)
            
print(r)

