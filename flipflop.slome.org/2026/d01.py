DAY,_,_=__file__.rpartition('.')

s1=s2=s3=0
r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        v=int(l)
        s1+=max(0,60-v)

        s2+=max(0,60-v)
        s2+=max(0,v-60)*5

        r+=v,

l=len(r)
for a,b in zip(r[:l//2],r[l//2:]):
    if a>b:
        s3+=5*(a-b)
    else:
        s3+=b-a

print(s1)
print(s2)
print(s3)