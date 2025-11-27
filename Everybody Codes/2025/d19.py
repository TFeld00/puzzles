DAY,_,_=__file__.rpartition('.')

from itertools import product
import re

def solve(part):
    r=[]

    with open(f'{DAY}{part}.txt','r')as F:
        for l in F:
            l=l.rstrip('\n')
            l=[*map(int,re.findall(r'-?\d+',l))]

            r+=[l]

    D={}
    for a,b,c in r:
        if a not in D:D[a]=[]
        D[a]+=[b,c],
    e=max(D)

    H={}
    for a,l in D.items():
        H[a]=[]
        for y,h in l:
            H[a]+=range(y,y+h)

    q={0:0}
    x=i=0
    for (x1,l1) in sorted(H.items()):
        q2={}
        w=x1-x
        x=x1
        i+=1
        for (h1,v),h2 in product(q.items(),l1):
            d=abs(h1-h2)
            if d>w:continue
            if d%2 != w%2: continue
            m=v+(w+h2-h1)//2
            q2[h2] = min(m,q2.get(h2,1e9))

        q=q2
        if part=='c' and i%10<1:
            print(end='.')
    if part=='c':print()
    print(min(q.values()))

solve('a')
solve('b')
solve('c')