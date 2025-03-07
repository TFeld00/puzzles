DAY,_,_=__file__.rpartition('.')


with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        
a=l
w=1
while w<=a:
    a-=w
    w+=2

print(w*(w-a))  

# --------------

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        
a=l
w=h=1
t=20240000
while w*h<=t:
    t-=w*h
    w+=2
    h=(h*a)%1111

print(w*(w*h-t))  

# --------------

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
  
a=l
w=h=1
T=202400000
aq=10
H=[h]
x=0
tot=1
while 1:
    w+=2
    h=(h*a)%aq+aq
    H=h,*[v+h for v in H],h
    tot=sum(H)-sum((a*w)*i%aq for i in H[1:-1])
    if tot>T:break

print(tot-T)

