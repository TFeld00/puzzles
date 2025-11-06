DAY,_,_=__file__.rpartition('.')

_pow = pow
from math import *
pow = _pow
from fractions import *

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]

s=2025
for a,b in zip(r,r[1:]):
    v = Fraction(a,b)
    s*=v
print(s)

# ----

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]

s=10000000000000
for a,b in zip(r,r[1:]):
    v = Fraction(b,a)
    s*=v
print(ceil(s))

# ----

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split('|'))]
        r+=[l]

s=100
for a,b in zip(r,r[1:]):
    v = Fraction(a[-1],b[0])
    s*=v
print(int(s))