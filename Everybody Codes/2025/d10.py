DAY,_,_=__file__.rpartition('.')

from functools import cache

# ---

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='D':x,y=j,i

q=[[x,y,4]]
c=set()
for x,y,d in q:
    c|={(x,y)}
    if d:
        for dx,dy in [-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]:
            a,b=x+dx,y+dy
            if (not (a,b) in c) and 0<=a<len(r[0]) and 0<=b<len(r):
                c|={(a,b)}
                q.append([a,b,d-1])

s=0
for x,y in c:
    s+= r[y][x]=='S'
print(s)

# ---

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

S=set()
H=set()
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='D':x,y=j,i
        if c=='S':S|={(j,i)}
        if c=='#':H|={(j,i)}

s=0
q=[[x,y]]
for _ in range(20):
    c=set()
    for x,y in q:
        for dx,dy in [-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]:
            a,b=x+dx,y+dy
            if (not (a,b) in c) and 0<=a<len(r[0]) and 0<=b<len(r):
                c|={(a,b)}

    s+=len((S&c)-H)
    S-=(c-H)
    S={(i,j+1)for i,j in S if j<len(r)-1}

    s+=len((S&c)-H)
    S-=(c-H)
    q=set(c)

print(s)

# ---

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
                
W,H=len(r[0]),len(r)

S=set()
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='D':x,y=j,i
        if c=='S':S|={(j,i)}

@cache
def f(x,y,s,t,d=0):
    s1=set(s)
    if not s:
        return 1
    for j,i in s:
        if all(r[k][j]=='#'for k in range(i,H)):
            return 0
    res=0
    if t==0: #sheep
        a=0
        for j,i in s1:
            if (j,i+1) != (x,y) or r[i+1][j]=='#':
                if i<H-1:
                    s2=s1-{(j,i)}|{(j,i+1)}
                    res+=f(x,y,tuple(s2),1,d+1)
                a=1
        if not a:
            res+=f(x,y,s,1)
    else: #dragon
        for dx,dy in [-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]:
            a,b=x+dx,y+dy
            if 0<=a<W and 0<=b<H:
                s2=s
                if (a,b) in s1 and r[b][a]!='#':
                    s2=s1-{(a,b)}
                res+=f(a,b,tuple(s2),0,d+1)
    return res

print(f(x,y,tuple(S),0))

