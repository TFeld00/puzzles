DAY,_,_=__file__.rpartition('.')

s1=s2=s3=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        w=len(l)//2
        s1+=w
        if w%2==0:
            s2+=w
        if 'e' not in l:
            s3+=w

print(s1)
print(s2)
print(s3)