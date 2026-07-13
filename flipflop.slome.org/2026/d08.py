DAY,_,_=__file__.rpartition('.')

r=[]
with open(f'{DAY}.txt', 'r') as F:
    for l in F:
        l=l.rstrip('\n')
        r+=l.split(),

from collections import Counter
R={}
for a,*l in r:
    v=dict(Counter(l))
    if a not in R:
        R[a]=v

d={'A':1,'B':1}
for i in range(7):
    n={}
    for a,b in d.items():
        x=R[a]
        for v,w in x.items():
            n[v]=n.get(v,0)
            n[v]+=b*w
    d=n
print(sum(d.values()))

# ---
# 
R={}
for a,b,*l in r:
    R[(a,b)]=l
    R[(b,a)]=l
l=['A','B']
for i in range(7):
    l2=[]
    for a,b in zip(l,l[1:]):
        l2+=a,*R.get((a,b),[])
    l2+=b,
    l=l2
print(len(l))

# ---
R={}
for a,b,*l in r:
    R[(a,b)]=l
    R[(b,a)]=l
d={('A','B'):1}
for i in range(21):
    n={}
    for (a,b),c in d.items():
        x=R[(a,b)]
        for v in zip([a,*x],[*x,b]):
            n[v]=n.get(v,0)
            n[v]+=c
    d=n
print(sum(d.values())+1)
