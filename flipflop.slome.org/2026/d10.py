DAY,_,_=__file__.rpartition('.')

ins=[]
labels={}
with open(f'{DAY}.txt', 'r') as F:
    i=-1
    for l in F:
        i+=1
        l=l.rstrip('\n')
        if l[:2]=='ba':
            x=[len(v)//2 for v in l[2:].split('ne')]
            ins+=x,
        elif l[:2]=='be':
            x=len(l[2:])//2
            labels[x]=i
            ins+=[-1],


def exec(r,j):
    o,*i=ins[j]
    if o==0:
        v,d=i
        r[d]=v
        r[d]%=65536
    elif o==1:
        s,d=i
        r[d]=r[s]
        r[d]%=65536
    elif o==2:
        a,b,d=i
        r[d]=r[a]+r[b]
        r[d]%=65536
    elif o==3:
        a,b,d=i
        r[d]=r[a]-r[b]
        r[d]%=65536
    elif o==4:
        a,b,d=i
        r[d]=r[a]*r[b]
        r[d]%=65536
    elif o==5:
        a,b,d=i
        r[d]=r[a]%r[b] if r[b]>0 else 0
        r[d]%=65536
    elif o==6:
        d=i[0]
        r[d]+=1
        r[d]%=65536
    elif o==7:
        d=i[0]
        r[d]-=1
        r[d]%=65536
    elif o==8:
        a=i[0]
        return labels[a]
    elif o==9:
        a,b=i
        if r[a]==0:
            return labels[b]
    elif o==10:
        a,b=i
        if r[a]!=0:
            return labels[b]
    return j

def run(r):
    j=s=0
    while j<len(ins):
        j=exec(r,j)+1
        s+=1
        if s>5000000:
            return 1
    return 0

r=[0]*16
run(r)
print(r[0])


# ---
res=0
for v in range(100):
    print(end='.')
    r=[0]*16
    r[0]=v
    res+=run(r)
print()
print(res)

# ---

D={
    0: 20480,
    1: 0,
    2: 61440,
    3: 0,
    4: 0,
    5: 4096,
    6: 53248,
    7: 0,
    8: 8192,
    9: 8192,
    10: 65536,
    11: 0,
    12: 8192,
    13: 0,
    14: 49152,
    15: 4096,
}

def slow(j):
    if j in D:
        sm=D[j]
        return sm
    x=[]
    diffs=[]
    for v in range(100):
        r=[0]*16
        r[0]=v
        r[1]=j
        w=run(r)
        if w:
            x+=v,
            l=len(x)
            if l>1:
                diffs+=x[-1]-x[-2],
        l=len(diffs)
        if len(set(diffs))>1 and l>3 and diffs[:l//2]==diffs[l//2:]:
            break

    sm=0
    if diffs:
        v=x[0]
        di=0
        while v<=(1<<16):
            sm+=v<(1<<16)
            v+=diffs[di%len(diffs)]
            di+=1
    return sm


def fast(j):
    if j in D:
        sm=D[j]
        return sm
    sm=0
    print(j,end=': ')
    for v in range(16):
        r=[0]*16
        r[0]=v
        r[1]=j
        sm+=run(r)
        print(end='.')
    print(sm*4096)
    return sm*4096

# SUM=0
# for j in range(16):
#     SUM+=slow(j)
# print(SUM)

SUM=0
for j in range(16):
    SUM+=fast(j)
print(SUM)

