DAY,_,_=__file__.rpartition('.')

from collections import Counter

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(',')
        l=[*map(int,l)]

print(sum(set(l)))

# ---

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(',')
        l=[*map(int,l)]

print(sum(sorted(set(l))[:20]))

# ---

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(',')
        l=[*map(int,l)]

print(max(Counter(l).values()))