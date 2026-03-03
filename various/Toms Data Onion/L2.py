DAY,_,_=__file__.rpartition('.')

import base64

t=''
with open(f'{DAY}_i.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        t+=l

with open(f'{DAY}_o.txt','wb')as F:
    b = base64.a85decode(t[2:-2])
    bytes_as_bits = [format(byte, '08b') for byte in b]
    s = [b[:7] for b in bytes_as_bits if b[:7].count('1')%2==int(b[7])]
    s=''.join(s)
    l=len(s)//8
    F.write(int(s,2).to_bytes(l))
    