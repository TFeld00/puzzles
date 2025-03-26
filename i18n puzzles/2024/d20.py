DAY,_,_=__file__.rpartition('.')

_pow = pow
from math import *
pow = _pow

t=''

with open(f'{DAY}.txt', 'r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        t+=l

import base64
b=base64.b64decode(t)

s=b.decode('utf-16le')[1:]

w=20
ba=['{:020b}'.format(ord(c)) for c in s]
#print(ba)
#print([len(v)for v in ba])
ba=''.join(ba)
#print(ba)
#print(len(ba)/16)

w=8
r=[]
for i in range(0,len(ba),w):
    r+=int(ba[i:i+w],2),
#print([hex(v)for v in r])

b=bytes(r)
#print(b)
#print(bin(0xfc))

def utf8e(b):
    def con(b,i,n):
        if n>1:
            v=''.join(['{:06b}'.format(b[i+v]%64) for v in range(1,n)][::1])
        else:
            v='{:08b}'.format(b[i]%64)

        l=ceil(len(v)/8)*8
        l=28
        return v.rjust(l,'0')[-28:],
    i=0
    r=[]
    while i<len(b):
        c=b[i]
        if c<0b11000000:
            r+=con(b,i,1)
            i+=1
        elif c<=0b11011111:
            r+=con(b,i,2)
            i+=2
        elif c<=0b11101111:
            r+=con(b,i,3)
            i+=3
        elif c<=0b11110111:
            r+=con(b,i,4)
            i+=4
        elif c<=0b11111011:
            r+=con(b,i,5)
            i+=5
        elif c<=0b11111101:
            r+=con(b,i,6)
            i+=6
        elif c<=0b11111110:
            r+=con(b,i,7)
            i+=7
    r=''.join(r)
    x=[]
    for i in range(0,len(r),8):
        x+=int(r[i:i+8],2),
    return x

x=utf8e(b)

print(bytes(x))
print(bytes(x).decode('utf8'))

# "2\x0396486,\x00456935\x07, 0144\x0152"
# -> "2396486,4569357, 0144152"