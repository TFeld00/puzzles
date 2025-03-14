DAY,_,_=__file__.rpartition('.')

from collections import Counter
from unidecode import unidecode

s=0

def valid(s):
    s=unidecode(s).lower()
    if len(s)<4:return False
    if len(s)>12:return False
    if not any(c in 'aeiou' for c in s):return False
    if not any(c.isalpha() and (c not in 'aeiou')for c in s):return False
    if not any(c.isdigit()for c in s):return False
    if any(a.isalpha() and b>1 for a,b in Counter(s).items()):return False
    return True

with open(f'{DAY}.txt', 'r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        
        s+=valid(l)
        

print(s)