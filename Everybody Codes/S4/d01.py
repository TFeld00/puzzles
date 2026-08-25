DAY,_,_=__file__.rpartition('.')


r=[]
s=0
t=''

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split(','))]
        r+=[l]

for l in r:
    v={0}
    i=0
    for x in l:
        if i-x<0 or i-x in v:
            i+=x
        else:
            i-=x
        v|={i}
    s+=i
print(s)

# ---


r=[]
s=0
t=''

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split(','))]
        r+=[l]

for l in r:
    v={0}
    i=0
    for x in l:
        if i-x<0 or i-x in v:
            i+=x
            while i in v:
                i+=1
        else:
            i-=x
        v|={i}
    s+=i
print(s)

# ---


r=[]
s=0
t=''

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split(','))]
        r+=[l]

for l in r:
    v={0}
    w=set()
    i=0
    u=1
    for x in l:
        j=i
        u=-u
        if i-x<0 or i-x in v or any((i-x<a<j<b or a<i-x<b<j) and u==q for a,b,q in w):
            i+=x
            while i in v or any(j<a<i<b and u==q for a,b,q in w):
                i+=1
            if any(a<=j<=b<=i and u==q for a,b,q in w):
                i=j
                u=-u
                continue
        else:
            i-=x
        v|={i}
        w|={(*sorted([j,i]),u)}
    s+=i
print(s)