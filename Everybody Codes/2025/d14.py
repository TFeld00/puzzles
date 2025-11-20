DAY,_,_=__file__.rpartition('.')

##  --- ---

from itertools import cycle, pairwise
from alg.cellular import step_dict, step_list, to_dict, to_lists, step_function_game_of_life

def get_diags_list(m:list, y, x, default):
    for dy in (-1, 1):
        for dx in (-1,  1):
            X, Y = x+dx, y+dy
            if 0 <= X < len(m[0]) and 0 <= Y < len(m):
                yield m[Y][X]
            else:
                yield default

F1=lambda c,n:(sum(n)%2) if c else (sum(n)%2<1)


##  --- ---


r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[c=='#'for c in l]
        r+=[l]

t=0
for _ in range(10):
    r=step_list(r,step_function=F1,default=0, expandable=False, get_neigbors_function=get_diags_list)
    t+=sum(sum(l) for l in r)

print(t)


##  --- ---


r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[c=='#'for c in l]
        r+=[l]

t=0
for _ in range(2025):
    r=step_list(r,step_function=F1,default=0, expandable=False, get_neigbors_function=get_diags_list)
    t+=sum(sum(l) for l in r)

print(t)


##  --- ---


r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[c=='#'for c in l]
        r+=[l]
        
        
W,H=len(r[0]),len(r)
r1 = [l[:]for l in r]

r=[[0]*34 for _ in range(34)]

def center(a,b):
    return all(
        a[13+i][13:21]==b[i]
        for i in range(8)
    )

t=0
D={}
L=0
R=[0]
S=[0]
for _ in range(1000000000):
    r=step_list(r,step_function=F1,default=0, expandable=False, get_neigbors_function=get_diags_list)
    if center(r,r1):
        print(_,end='.')
        T=sum(map(tuple,r),tuple())
        R+=[_]
        if T in D:
            L=_
            break
        D[T]=_
        S+=[sum(sum(l) for l in r)]
        t+=S[-1]

i=R.index(D[T])
D=[b-a for a,b in pairwise(R[i:])]

C=cycle(D)
CS=cycle(S[i:])
a=L
while L<1000000000:
    v=next(CS)
    t+=v
    w=next(C)
    L+=w

print()
print(t)
