DAY,_,_=__file__.rpartition('.')

from fractions import *

def will_cross(a1, b1, delta_a, delta_b):
        d = (b1 - a1) % 1
        rel_move = delta_b - delta_a

        if a1==b1:return 0
        if d == 0:
            return abs(rel_move) >= 1

        if rel_move > 0:
            return d + rel_move >= 1
        if rel_move < 0:
            return d + rel_move <= 0

        return 0

def solve(h,d,c,m):
    h=[*map(int,h)]
    d=[5-2*len(v) for v in d]
    c=[*map(int,c)]
    m=[*map(int,m)]

    hands = [Fraction(a,b)for a,b in zip(c,h)]
    dirs = [Fraction(a,b)for a,b in zip(d,h)]

    res_t=0
    res=0
    init = hands[:]
    M=mh=sum(v>0 for v in m)
    i=0
    while 1:
        i+=1
        if not M:break
        for x,y in [1,0],[1,2],[0,2]:
            res += will_cross(hands[x],hands[y],dirs[x]*(m[x]>0),dirs[y]*(m[y]>0))

        for j in range(len(hands)):
            if m[j]>0:
                hands[j]=(hands[j]+dirs[j])%1
                m[j]-=1
                if not m[j]:mh-=1
        if mh < M: # reset cycle detection
            M=mh
            init=hands[:]
            res_t+=res
            res=0
            i=0
        elif hands == init: # cycle!
            if mh:
                mul = min((v for v in m if v))//i
                skip = mul*i
                res*=mul+1
                m=[v-skip if v else v for v in m]
                mh=sum(v>0 for v in m)
    return res+res_t

for part in 'abc':
    r=[]

    with open(f'{DAY}{part}.txt','r')as F:
        for l in F:
            l=l.rstrip('\n')
            if l:
                a,b=l.split()
                b=b.split(':')
                r+=[b]

    total=0
    i=0
    while r:
        i+=1
        h,d,c,m,*r  =r
        X=solve(h,d,c,m)
        total+=X
        if i%10<1:print(end='.')
    if i>9:print(end=' ')
    print(total)
