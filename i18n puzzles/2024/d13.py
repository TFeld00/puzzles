DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
import re

r=[]

with open(f'{DAY}.txt', 'r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

a,b=parse_no_headers(r)

for i in range(len(a)):
    s=a[i]
    by = bytearray([int(''.join(v),16)for v in zip(*[iter(s)]*2)])
    r=[]
    for enc in 'utf-16be','utf-16le','utf8','latin-1':
        try:
            s=by.decode(enc)
            if s.startswith('\ufeff') or s.startswith('\ufffe'):s=s[1:]
            if s.isalpha() and re.search('[a-z]',s):
                r+=[s]
        except:
            pass
    print(*r)
    a[i]=r[0]

s=0
for l in b:
    l=l.strip()
    print(l, end=' ')
    for i,w in enumerate(a,1):
        if re.match('^'+l+'$',w):
            s+=i
            print(w,i)
print(s)

