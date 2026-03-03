DAY,_,_=__file__.rpartition('.')

import base64
import itertools

t=''
with open(f'{DAY}_i.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        t+=l

with open(f'{DAY}_o.txt','w')as F:
    B = base64.a85decode(t[2:-2])
    B = [int(byte) for byte in B]
    
    key=[]
    for ki in range(32):
        l=B[ki::32]
        key+=[[v for v in range(256)if all(10==(b^v) or 31<(b^v)<127 for b in l)]][0]
    
    c=itertools.cycle(key)
    for b,x in zip(B,c):
        v=b^x
        
        F.write(chr(b^x))