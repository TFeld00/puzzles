DAY,_,_=__file__.rpartition('.')
from itertools import groupby

s=[]
with open(f'{DAY}.1.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=map(int,l)

def f(s):
    r=[]
    l=0
    for c in s:
        if c==l:
            r+=2,l
            l=0
        elif l:
            r+=1,l
            l=c
        else:
            l=c
    if l:
        r+=1,l
    return r

for _ in range(65):
    s=f(s)
    c='.'
    if _%10>8: c='!'
    elif _%10==4:c=','
    print(c,end='')
print()
print(len(s))


s=[]
with open(f'{DAY}.2.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=map(int,l)

for _ in range(65):
    s=f(s)
    c='.'
    if _%10>8: c='!'
    elif _%10==4:c=','
    print(c,end='')
print()
print(sum(len(list(l))==3 for _,l in groupby(s)))