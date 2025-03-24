DAY,_,_=__file__.rpartition('.')

import re

r=[]

with open(f'{DAY}.txt', 'r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
def clean(s):
    s=re.sub(r'[\u2067\u2066\u2069]','',s)
    return s

T=str.maketrans('()',')(')
def flipTokens(m):
    s=str.translate(m[1],T)[::-1]
    return re.sub(r'\d+',lambda a:a[0][::-1],s)

def flip(s):
    while re.search(r'[\u2067\u2066\u2069]',s):
        s=re.sub(r'[\u2067\u2066]([^\u2067\u2066\u2069]*)\u2069',flipTokens,s)
    return s


total=0
for l in r:
    v=abs(eval(clean(l))-eval(flip(l)))
    total+=v
print(round(total))