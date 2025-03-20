DAY,_,_=__file__.rpartition('.')

from fractions import *
import japanese_numbers

r=[]

with open(f'{DAY}.txt', 'r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
def getUnits(s):
    d={
        '尺':1,
        '間':6,
        '丈':10,
        '町':360,
        '里':12960,
        '毛':Fraction(1,10000),
        '厘':Fraction(1,1000),
        '分':Fraction(1,100),
        '寸':Fraction(1,10),
        }
    for c in s:
        if c in d:
            yield d[c]*Fraction(10,33)

s=0

for l in r:
    a,b = japanese_numbers.to_arabic_numbers(l)
    ua,ub = getUnits(l)
    x=(a*ua*b*ub)
    s+=x

print(s)
