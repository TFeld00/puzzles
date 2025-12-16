DAY,_,_=__file__.rpartition('.')

from itertools import pairwise

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split(','))]
        r+=[l]

s1=0
s2=0
for (x,y),(a,b) in pairwise([[0,0]]+r):
    q,w=abs(x-a),abs(y-b)
    s1+=q+w
    s2+=max(q,w)
print(s1)
print(s2)


s3=0
for (x,y),(a,b) in pairwise(sorted([[0,0]]+r, key=lambda v:sum(v))):
    q,w=abs(x-a),abs(y-b)
    s3+=max(q,w)
print(s3)