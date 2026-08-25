DAY,_,_=__file__.rpartition('.')

from functools import cache

r={}
msg=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        if '#' in l:
            a,b,c=[v[1:]for v in l.split()]
            r[a]=int(b),int(c)
        elif l:
            msg+=map(int,l.split(','))

@cache
def f(curr,seen):
    if curr=='D':return 1
    res=0
    x,y=r[curr]
    for i in r:
        v=1<<int(i if i.isdigit() else 0 if i=='S' else len(r))
        X,Y=r[i]
        if abs(X-x)+abs(Y-y)>5:
            continue
        if seen&v:
            continue
        res+=f(i,seen|v)
    return res
        
print(f('S',1))