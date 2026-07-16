DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}.txt', 'r') as F:
    i=-1
    for l in F:
        r+=l,

trees=[]
for i in range(0,len(r),3):
    a,b = r[i:i+2]
    a=a.split()
    b=b.split()
    tr={}
    for j in range(0,len(b),3):
        x,y,z=b[j:j+3]
        q=a[j//3]
        
        x=int(x)if x.isdigit() else -1
        z=int(z)if z.isdigit() else -1
        q=int(q)if q.isdigit() else -1
        tr[int(y)] = [x,z,q]
    trees+=tr,
# ---

def size(sp,st):
    return len(sp) + sum(map(len,st.values()))



def other_t(trs,i):
    all_t=set()
    for I,(tr,sp,st) in enumerate(trs):
        if I==i:continue
        all_t |= {*sp.keys()}
        all_t |= {(x,y)for x in st for y in st[x]}
    return all_t

def other_st(trs,i):
    all_t={}
    for I,(tr,sp,st) in enumerate(trs):
        #if I==i:continue
        for x in st:
            all_t[x]=all_t.get(x,set())|st[x]
    return all_t

def calc_E2(st,trs,i):
    s=0
    L=other_st(trs,i)
    for x,l in st.items():
        a=L[x]
        l=[[v in l,min(10,v)]for v in sorted(a)[-3:]]
        m=[1,2,3][-len(l):]
        s+=sum(a*b*c for (a,b),c in zip(l,m))
    return s

def print_trees(trs):
    a=other_t(trs,-1)
    x,y = zip(*a)
    o=min(x)
    m=['']
    for y in range(min(y),max(y)+1):
        l=[' ']*(max(x)-min(x)+1)
        m+=l,
    for I,(tr,sp,st) in trs.items():
        if I==i:continue
        for x,y in sp.keys():
            m[y][x-o]=chr(I+65)
        for x in st:
            for y in st[x]:
                m[y][x-o]=chr(I+97)
    with open(f'{DAY}.o.txt', 'w') as F:
        for l in m[::-1]:
            F.write(''.join(l)+'\n')

def run(trees, gens = 1):
    trs = []
    for i,tr in enumerate(trees):
        sp={(i*10,1):0}
        st={}
        trs+=[tr,sp,st],
        
    for _ in range(gens):
        dead=set()
        total = 0

        next={}
        for I,(tr,sp,st) in enumerate(trs):
            for (x,y) in sp:
                if x in next and next[x][0]>y:
                    pass
                else:
                    next[x]=[y,tr,{(x,1):0},{}]
        trs=[[tr,sp,st] for _,(_,tr,sp,st) in sorted(next.items())]

        for Y in range(1,101):
            if len(dead)==len(trs):break
            #grow
            for I,(tr,sp,st) in enumerate(trs):
                if I in dead:
                    continue
                next={}
                others = other_t(trs,I)
                for (x,y),i in sp.items():
                    a,b,c=tr[i]
                    n=(x-1,y,a),(x+1,y,b),(x,y+1,c)
                    for dx,dy,v in n:
                        if v>=0:
                            if (dx,dy) not in others and dy not in st.get(dx,set()):
                                next[(dx,dy)] = max(next.get((dx,dy),-1),v)
                    st[x]=st.get(x,set())|{y}
                trs[I][1]=next
            #energy
            for I,(tr,sp,st) in enumerate(trs):
                if I in dead:
                    continue
                if Y>=5:
                    E=calc_E2(st,trs,I)
                    e_needed = 3 * size(sp,st)
                    if E<e_needed:
                        dead|={I}
    for I,(tr,sp,st) in enumerate(trs):
        total += size(sp,st)
        
    return total

# ---

print(sum(run([t]) for t in trees))

print(run(trees))

print(run(trees,3))
