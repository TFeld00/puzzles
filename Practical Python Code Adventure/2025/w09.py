DAY,_,_=__file__.rpartition('.')

import re

def solve(part):
    r=[]
    with open(f'{DAY}.{part}.txt','r', encoding='utf8')as F:
        for l in F:
            l=l.rstrip('\n')
            r+=l,

    s,t=map(int,r[0].split(','))
    e={}
    for l in r[:]:
        a,*b=map(int,re.split(',|:',l))
        e[a]=b

    q=[(s,1)]
    seen={s}
    for n,l in q:
        if n==t:
            print(l)
            break
        for v in e.get(n):
            if v not in seen:
                seen|={v}
                q+=(v,l+1),

# ---

solve(1)

# ---

solve(2)
