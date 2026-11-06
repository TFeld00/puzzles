DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(', ')
        l=[int(v.split('=')[1]) for v in l]
        r+=[l]
        
        
def f(i,g,l):
    b=[0]
    t=0
    s=0
    while 1:
        if t+sum(b)>=l:break
        n=[]
        for v in b:
            v+=1
            if v>=g:
               a=v//2
               n+=a,1,v-a-1
               t+=1
            else:
               n+=v,
        s+=1
        b=n
    return s

s=0
for v in r:
    s+=f(*v)
print(s)

# ---

r=[]
s=0
t=''

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(', ')
        l=[int(v.split('=')[1]) for v in l]
        r+=[l]

def f(i,g,l):
    n={0:1}
    lv=1
    s=0
    while 1:
        if lv>=l:break
        h=g//2
        mx=max(n.keys())
        k=g-mx
        n={v+k:y for v,y in n.items()}
        x=n.pop(g)
        n[h]=n.get(h,0)+2*x
        n[1]=n.get(1,0)+1*x
        lv+=x
        s+=k
    return s

s=0
for v in r:
    s+=f(*v)
print(s)

# ---

r=[]
s=0
t=''

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(', ')
        l=[int(v.split('=')[1]) for v in l]
        r+=[l]
        

def f(i,g,l):
    n={0:1}
    lv=1
    s=0
    while 1:
        if lv>=l:break
        h=g//2
        mx=max(n.keys())
        k=g-mx
        n={v+k:y for v,y in n.items()}
        x=n.pop(g)
        n[h]=n.get(h,0)+2*x
        n[1]=n.get(1,0)+1*x
        lv+=x
        s+=k
    return s

s=0
for v in r:
    s+=f(*v)
print(s)
