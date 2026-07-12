DAY,_,_=__file__.rpartition('.')

r=[]
with open(f'{DAY}.txt', 'r') as F:
    for l in F:
        l=l.rstrip('\n')
        r+=l,

# ---

PR=0
DEB=0
def print_deb(*l,end=None):
    if not PR:return
    print(*l,end=end)
def print_sn():
    if not DEB:return
    xy=sn[:]
    xy+=(x,y),
    if i<len(S):xy+=S[i],
    px,py=zip(*xy)
    for dj in range(max(py),min(py)-1,-1):
        line=''
        for di in range(min(px),max(px)+1):
            if (di,dj)in sn:line+='#'
            elif (di,dj)==(x,y):line+='S'
            elif i<len(S) and (di,dj)==S[i]:line+='@'
            else:line+=' '
        print(line)
    print()

# ---

M,_,*c=r
S=[]
for l in c:
    x,y = l.split(',')
    S+=(int(x),int(y)),

# ---

PR=0
DEB=0

s=0
x,y=0,0
i=0
L=len(M)
for m in M[:L//2]:
    if (x,y)==S[i]:
        i+=1
    dx,dy=[(-1,0),(0,1),(1,0),(0,-1)]['<^>v'.find(m)]
    x+=dx
    y+=dy
print(i)

# ---

PR=0
DEB=0

s=0
x,y=0,0
i=0
sn=[]
L=len(M)
for m in M[:L//2]:
    if (x,y)==S[i]:
        i+=1
    dx,dy=[(-1,0),(0,1),(1,0),(0,-1)]['<^>v'.find(m)]
    sn+=(x,y),
    x+=dx
    y+=dy
    if len(sn)>i:sn.pop(0)
    print_deb(x,y,sn)
    if (x,y) in sn:break
    print_sn()
print(i+1)

# ---

PR=0
DEB=0

s=0
x,y=0,0
i=0
E=0
sn=[]
L=len(M)

for m in M:
    print_deb(m,x,y,end=' ')

    dx,dy=[(-1,0),(0,1),(1,0),(0,-1)]['<^>v'.find(m)]
    px,py=x,y
    x+=dx
    y+=dy
    if i<len(S) and (x,y)==S[i]:
        i+=1

        s+=1

    print_deb(m,x,y,end=' ')

    if (x,y) in sn:
        j=sn.index((x,y))+1
        if j>1:
            if PR:print(['j',j],end=' ')
            sn=sn[j:]
            s=len(sn)
            E+=1
    sn+=(px,py),
    while len(sn)>s:sn.pop(0)
    
    print_deb(s,i,sn,S[i]if i<len(S) else'')
    print_sn()

print((s+1)*E)