DAY,_,_=__file__.rpartition('.')

from datetime import *

d={}

with open(f'{DAY}.txt', 'r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')

        a,b=l.split(': ')
        p=b.split(', ')
        a=[*map(int,a.split('-'))]
        for v in p:
            d[v]=(d.get(v,[])+[a])
        

def valid(a):
    a,b,c=a
    try:
        a = 1900+a if a>19 else 2000+a
        d=datetime(a,b,c)
        return True
    except:
        return False
    
r=set()


for p in d:
    for f in [
        lambda a:[a[0],a[1],a[2]],
        lambda a:[a[0],a[2],a[1]],   
        lambda a:[a[2],a[0],a[1]],
        lambda a:[a[2],a[1],a[0]],
    ]:
        l=[f(x)for x in d[p]]
        if all(valid(x)for x in l):
            if [1,9,11] in l:
                r|={p}

print(' '.join(sorted(r)))
