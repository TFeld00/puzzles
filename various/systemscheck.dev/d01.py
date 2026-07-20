DAY,_,_=__file__.rpartition('.')

s1=s2=s3=0

r=[]

t=0
with open(f'{DAY}.txt','r')as F:
    for l in F:
        a,b,c=l.split()
        a=int(a[2:])
        b=int(b[1:])
        c=c>'e'
        r+=[a,b,c],

res=[]
d={}
for a,b,c in r:
    if c:
        res+=[a-d[b],b],
        del d[b]
    else:
        d[b]=a
    t=max(t,a)+1
for b,v in d.items():
    res+=[t-v,b],
print(max(res)[0])

rt,rv=0,0
t=v=0
for a,b,c in r:
    if c:
        if v>rv:
            rt=a-t
            rv=v
        v-=1
        t=a
    else:
        v+=1
        t=a
print(rt)