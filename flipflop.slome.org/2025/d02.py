DAY,_,_=__file__.rpartition('.')

from itertools import groupby

t=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')

        t+=l


r1=[]
r2=[]
r3=[]
p1=0
p2=m2=0
p3=0
x2=''
fib=[0]
a,b=0,1
for i in range(50):
    a,b=b,a+b
    fib+=a,

for c in t:
    if c=='^':p1+=1
    if c=='v':p1-=1
    r1+=[p1]

    if c!=x2:m2=0
    x2=c
    m2+=1
    if c=='^':p2+=m2
    if c=='v':p2-=m2
    r2+=[p2]
for c,v in groupby(t):
    v=len([*v])
    if c=='^':p3+=fib[v]
    if c=='v':p3-=fib[v]
    r3+=[p3]
        
        
print(max(r1))
print(max(r2))
print(max(r3))