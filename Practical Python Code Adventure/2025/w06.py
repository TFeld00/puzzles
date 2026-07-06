DAY,_,_=__file__.rpartition('.')

from collections import Counter
import math

def solve(part):
    r=[]
    with open(f'{DAY}.{part}.txt','r', encoding='utf8')as F:
        for l in F:
            l=l.rstrip('\n')
            r+=l,
    u,*r=r
    u=[(*map(float,v.split(',')),) for v in u.split()]
    r2=[]
    for v in r:
        *x,z=v.split(',')
        r2+=(*map(float,x),z),

    s=[]
    for p1 in u:
        l=sorted((math.dist(p1,p2),z) for *p2,z in r2)[:7]
        s+=Counter(v for *_,v in l).most_common(1)[0][0],
    return s

# ---

print(''.join(v[0]for v in solve(1)))

# ---

print(*solve(2))
