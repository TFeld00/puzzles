DAY,_,_=__file__.rpartition('.')

_pow = pow
from math import *
pow = _pow

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split())]
        r+=[l]

s1=0
for x,y in r:
    s1+=comb(x+y-2,x-1)
print(s1)

s2=0
for x,y in r:
    x,y,z=x-1,y-1,x-1
    s2+=factorial(x+y+z)//(factorial(x)*factorial(y)*factorial(z))
print(s2)

s3=0
for x,y in r:
    y-=1
    s3+=factorial(x*y)//(factorial(y)**x)
print(s3)