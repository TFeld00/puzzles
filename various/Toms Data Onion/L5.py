DAY,_,_=__file__.rpartition('.')

import base64
import lib.wrap

t=''
with open(f'{DAY}_i.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        t+=l

with open(f'{DAY}_o.txt','wb')as F:
    b = base64.a85decode(t[2:-2])
    b = [format(byte, '08b') for byte in b]
    
    kek,b=b[:32],b[32:]
    eiv,b=b[:8],b[8:]
    wrk,b=b[:40],b[40:]
    kiv,b=b[:16],b[16:]

    unwr = lib.wrap.unwrap(kek,wrk,eiv)
    print(len(unwr))