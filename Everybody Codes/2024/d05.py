DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split())]
        r+=[l]
        

rows = *map(list,zip(*r)),
L=len(rows)
for i in range(10):
    c=rows[i%L].pop(0)
    j=-1
    d=1

    for x in range(c):
        j+=d
        if j>len(rows[(i+1)%L]):
            d=-d;j-=2
        elif j<0:
            d=-d;j+=2
    rows[(i+1)%L].insert(j,c)
print(''.join(map(str,[l[0]for l in rows])))


# ------------------


r=[]
with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split())]
        r+=[l]

rows = *map(list,zip(*r)),
L=len(rows)
D={}
i=0
while 1:
    c=rows[i%L].pop(0)
    j=-1
    d=1

    for x in range(c):
        j+=d
        if j>len(rows[(i+1)%L]):
            d=-d;j-=2
        elif j<0:
            d=-d;j+=2
    rows[(i+1)%L].insert(j,c)
    n=int(''.join(map(str,[l[0]for l in rows])))
    D[n]=D.get(n,0)+1
    i+=1
    if D[n]==2024:break
    
print(n*i)

# ------------------

r=[]
with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split())]
        r+=[l]

rows = *map(list,zip(*r)),
L=len(rows)
D=set()
N=set()
i=0
while 1:
    c=rows[i%L].pop(0)
    j=-1
    d=1

    for x in range(c):
        j+=d
        if j>len(rows[(i+1)%L]):
            d=-d;j-=2
        elif j<0:
            d=-d;j+=2
    rows[(i+1)%L].insert(j,c)
    n=int(''.join(map(str,[l[0]for l in rows])))
    N|={n}
    state = (*map(tuple,rows),)
    if state in D:break
    D|={state}
    i+=1
    
print(max(N))