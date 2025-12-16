DAY,_,_=__file__.rpartition('.')

t=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        t+=l
        

d={}
for i,c in enumerate(t):
    if c not in d:d[c]=[]
    d[c]+=i,
d2={}
for i,j in d.values():
    d2[i]=j
    d2[j]=i

s1=0
i=0
s3=0
v=set(t)
while i<len(t):
    v-={t[i]}
    x1=d2[i]
    s1+=abs(i-x1)
    s3+=abs(i-x1) * (1 if t[i].islower() else -1)
    i=x1
    i+=1
print(s1)
print(''.join(sorted(v,key=t.index)))
print(s3)