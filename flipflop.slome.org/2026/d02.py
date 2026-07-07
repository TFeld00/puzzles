DAY,_,_=__file__.rpartition('.')

s=''
with open(f'{DAY}.txt', 'r') as F:
    for l in F:
        l=l.strip()
        s+=l


w=[0]*100
i=0
for c in s:
    if c=='>':i+=1
    else:i-=1
    i%=100
    w[i]+=1

i=w.index(max(w))+1
print(i*max(w))


w=[0]*100
i=j=0
r=0
for c,C in zip(s,s[::-1]):
    if c=='>':i+=1
    else:i-=1
    i%=100
    if C=='>':j+=1
    else:j-=1
    j%=100
    if i==j:r+=1
    else:    w[i]+=1

print(r)