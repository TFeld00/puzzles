DAY,_,_=__file__.rpartition('.')

import re

r=[]
with open(f'{DAY}.1.txt','r', encoding='utf8')as F:
    for l in F:
        r+=map(int,re.findall(r'\d+',l))

l=len(r)-1

f=0
while l:
    i=r.index(max(r[:l+1]))
    if i<l:
        if i:
            r[:i+1] = r[:i+1][::-1]
            f+=1
        r[:l+1] = r[:l+1][::-1]
        f+=1
    l-=1
print(f)
# ---

r=[]
with open(f'{DAY}.2.txt','r', encoding='utf8')as F:
    for l in F:
        r+=map(int,re.findall(r'-?\d+',l))

l=len(r)-1

f=0
while l:
    i=r.index(max(r[:l+1], key=abs))
    v=r[i]
    if i==l and v>0:
        l-=1
        continue
    if i:
        r[:i+1] = [-x for x in r[:i+1][::-1]]
        f+=1
    if r[0]>0:
        r[0]=-r[0]
        f+=1
    r[:l+1] = [-x for x in r[:l+1][::-1]]
    f+=1
    l-=1
print(f)