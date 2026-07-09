DAY,_,_=__file__.rpartition('.')

r=[]
with open(f'{DAY}.txt', 'r') as F:
    for l in F:
        l=l.rstrip('\n')
        r+=l,

h=len(r)-1-400
s=0
for l in r[:h]:
    s+='o' in l
print(s)

# ---

s=0
side=0
for l in r:
    if 'o' in l:
        j=l.index('o')-2
        if side and j!=side:
            s+=1
        side=j
print(s)

# ---

w=0
while 1:
    side=0
    s=0
    for i in range(len(r)):
        l=r[i]
        if 'o' in l:
            s+=1
            j=l.index('o')-2
            if j!=side:
                r[i]='  |'
            side=j
    if s:
        w+=1
    else:break
print(w)
