DAY,_,_=__file__.rpartition('.')

from fractions import *
import re
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

# manual parsing
N='一二三四五六七八九十'
T={
    '百':100,
    '千':1000,
    '万':10000,
    '億':100000000,
}

def parse(s):
    d=dict(T)
    for i,c in enumerate(N,1):
        d[c]=i
    p=0
    for a,b in re.findall('([一二三四五六七八九]?)([十百千]?)',s):
        if a or b:
            p+=d.get(a,1)*d.get(b,1)
    return p

def getNumbers(s):
    c=N+''.join(T.keys())
    for n in re.findall(f'[{c}]+',s):
        t=0
        for a,b in re.findall(r'([^万億]*)(万|億)?',n):
            t+=parse(a)*T.get(b,1)
        yield t

s=0
for l in r:
    a,b = getNumbers(l)
    ua,ub = getUnits(l)
    x=(a*ua*b*ub)
    s+=x

print(s)