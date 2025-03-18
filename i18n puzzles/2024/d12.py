DAY,_,_=__file__.rpartition('.')

import re
from unidecode import *

r=[]

with open(f'{DAY}.txt', 'r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

def sortGen(s,pre,post, lower=True):
    s=re.sub('\d|[^,\w]','',s)
    if lower:s=s.lower()
    s=pre(s)
    s=unidecode(s)
    s=post(s)
    return s.split(',')

def sortE(s):
    return sortGen(
        s,
        lambda s:s.replace('æ','ae'),
        lambda s:s
    )

def sortS(s):
    return sortGen(
        s,
        lambda s:str.translate(s,str.maketrans('åäöæø','ABCBC')),
        lambda s:str.translate(s,str.maketrans('ABC','åäö'))
    )

def sortD(s):
    return sortGen(
        s,
        lambda s:s.replace('æ','ae'),
        lambda s:''.join(re.search('([^A-Z]*)([A-Z].*)',s).groups()[::-1]).lower(),
        lower=False
    )

le=sorted(r,key=sortE)
ls=sorted(r,key=sortS)
ld=sorted(r,key=sortD)

l=len(le)//2
f=lambda x:int(x[l].split(':')[1])

print(f(le),f(ls),f(ld))
p=f(le)*f(ls)*f(ld)
print(p)