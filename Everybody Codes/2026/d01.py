DAY,_,_=__file__.rpartition('.')


r=[]
with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split(','))]
        r+=l

s=0
for i in r:
    v=int(i**0.5)
    if v*v<i:v+=1
    s+=(v*v-i)
print(s)

# ---

r=[]
with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split(','))]
        r+=l

s=0
for i in r:
    v=i//4
    if v*4<i:v+=1
    if v<2:v=2
    s+=(v*4-i)
print(s)

# ---

r=[]
with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split(','))]
        r+=l
s=0
for i in r:
    v=int(i**0.5)
    if v%2<1:v+=1
    if v*v<9:v=3
    if v*v-1<i:v+=2
    s+=(v*v-1-i)
print(s)