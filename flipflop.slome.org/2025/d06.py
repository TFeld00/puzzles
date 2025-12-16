DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split(','))]
        r+=[l]        
        
W=H=1000
F=500
T=100

FL,FR=W//2-F//2,W//2+F//2

s1=sum((FL<=(x*T)%W<FR and FL<=(y*T)%H<FR) for x,y in r)
print(s1)

s2=0
for i in range(1,1001):
    T=3600*i
    s2+=sum((FL<=(x*T)%W<FR and FL<=(y*T)%H<FR) for x,y in r)
print(s2)

s3=0
for i in range(1,1001):
    T=31556926*i
    s3+=sum((FL<=(x*T)%W<FR and FL<=(y*T)%H<FR) for x,y in r)
print(s3)