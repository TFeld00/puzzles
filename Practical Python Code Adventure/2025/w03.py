DAY,_,_=__file__.rpartition('.')

r=[]
with open(f'{DAY}.1.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=l.replace('_',' ').split(',') if l else [],

p,i,*r=r
p=int(p[0])
t=[]

for x in i:
    o,n=x[0],int(x[1:])
    if o=='L':
        p-=n
    elif o=='R':
        p+=n
    elif o=='T':
        t+=r[p][:n]
        r[p]=r[p][n:]
    elif o=='D':
        r[p]+=t[:n]
        t=t[n:]

print(''.join([v[0]for v in r if v]))

# ---

r=[]
with open(f'{DAY}.2.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=l.replace('_',' ').split(',') if l else [],

p,i,*r=r
p=int(p[0])
t=[]

for x in i:
    o,n=x[0],int(x[1:])
    if o=='L':
        p-=n
    elif o=='R':
        p+=n
    elif o=='T':
        t+=r[p][:n]
        r[p]=r[p][n:]
        r=r[1:]+r[:1]
    elif o=='D':
        r[p]+=t[:n]
        t=t[n:]

print(''.join([v[0]for v in r if v]))
