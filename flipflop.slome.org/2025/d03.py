DAY,_,_=__file__.rpartition('.')

from collections import Counter

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

print(Counter(r).most_common(1)[0][0])

s2=0
s3=0
for c in r:
    r,g,b=map(int,c.split(','))
    if r<g>b and r!=b:s2+=1

    if r==g or g==b or r==b:s3+=10
    elif g<r>b:s3+=5
    elif r<g>b:s3+=2
    elif g<b>r:s3+=4
print(s2)
print(s3)
