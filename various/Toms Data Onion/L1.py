DAY,_,_=__file__.rpartition('.')

import base64

t=''
with open(f'{DAY}_i.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        t+=l

with open(f'{DAY}_o.txt','wb')as F:
    b = base64.a85decode(t[2:-2])
    bytes_as_bits = ''.join(format(byte, '08b') for byte in b)
    flipped = ''.join('10'[int(b)] if i%2 else b for i,b in enumerate(bytes_as_bits))
    rotated = flipped[-1:]+flipped[:-1]
    l=len(rotated)//8
    F.write(int(rotated,2).to_bytes(l))