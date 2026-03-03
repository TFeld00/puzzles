DAY,_,_=__file__.rpartition('.')

import base64

t=''
with open(f'{DAY}_i.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        t+=l



with open(f'{DAY}_o.txt','wb')as F:
    F.write(base64.a85decode(t[2:-2]))