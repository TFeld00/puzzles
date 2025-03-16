DAY,_,_=__file__.rpartition('.')

from itertools import *
from alg.util import  parse_no_headers
import bcrypt
from unicodedata import *

r=[]

with open(f'{DAY}.txt', 'r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        r+=[l]
        
a,b = parse_no_headers(r)

U={}
for x,s in a:
    U[x]=s

D={}
def valid1(u,p):
    if (u,p) not in D:
        x=bytes(U[u],'utf8')
        D[(u,p)]=bcrypt.checkpw(p,x)
    return D[(u,p)]

def valid(u,p):
    s=normalize('NFC',p)
    s=list(s)
    il = [i for i in range(len(s))if ord(s[i])>127]
    l = sum(ord(c)>127 for c in s)
    for i in product([0,1],repeat=l):
        s1=s[:]
        for j in range(l):
            if i[j]:
                s1[il[j]]=normalize('NFD',s[il[j]])
        s1=''.join(s1)
        if valid1(u,bytes(s1,'utf8')):
            return 1
    return 0
        
s=0
for i,l in enumerate(b):
    r=valid(*l)
    if i%40>38:
        print(end='.:'[i%400>398])
    s+=r
print()
print(s)
