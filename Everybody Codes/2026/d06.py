DAY,_,_=__file__.rpartition('.')


def f(d, null):
    q=[null]
    seen=set()
    for i in q:
        for b in d.get(i,set()):
            if b in seen:continue
            seen|={b}
            q+=b,

    return seen-{null}

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,b=l.split(':')
        b=b.split(',')
        r+=[[a,b]]

d={}
for a,b in r:
    d[a]=set(b)

print(len(f(d, 'NULL')))

# ---

r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,b=l.split(':')
        b=b.split(',')
        r+=[[a,b]]

d={}
for a,b in r:
    for v in b:
        d[v]=d.get(v,set())|{a}

print(len(f(d, 'NULL')))

# ---

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,b=l.split(':')
        b=b.split(',')
        r+=[[a,b]]

d={}
for a,b in r:
    for v in b:
        d[v]=d.get(v,set())|{a}

a,b,c=f(d,'NULLv1'),f(d,'NULLv2'),f(d,'NULLv3')

r=(a&b)|(b&c)|(a&c)

print(len(r))