DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
import re

r=[]

with open(f'{DAY}.txt', 'r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
a,b=parse_no_headers(r)

def decode(s):
    s=s.encode('latin-1').decode('utf8')
    return s

for j in 3,5:
    for i in range(j-1,len(a),j):
        a[i]=decode(a[i])

s=0
for l in b:
    l=l.strip()
    for i,w in enumerate(a,1):
        if re.match('^'+l+'$',w):
            s+=i
print(s)

