DAY,_,_=__file__.rpartition('.')

import re

r=[]
with open(f'{DAY}.txt', 'r') as F:
    for l in F:
        l=l.rstrip('\n')
        r+=l,


def score(p,part):
    v=0
    if re.search(r'[a-z]',p):v+=1
    if re.search(r'[A-Z]',p):v+=1
    if re.search(r'[0-9]',p):v+=1

    if part ==1:
        return len(p)*v

    if {*re.findall(r'[0-9]',p)}=={'7'}:v+=7
    x=re.findall(r'(.)(\1\1+)',p)
    if x:
        v+=max(map(lambda w:len(w[0]+w[1]),x))**2
    if re.search(r'red|green|blue',p):v*=3

    return len(p)*v

s=[]
for p in r:
    v=0
    s+=[score(p,1),p],
print(max(s)[1])


s=[]
for p in r:
    s+=[score(p,2),p],
print(max(s)[1])


s=[]
for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
    s+=[sum(score(p+c,2) for p in r) ,c],
print(max(s)[0])