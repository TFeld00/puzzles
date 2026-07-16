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

def calc_E(st):
    s=0
    for l in st.values():
        l=[min(10,v)for v in sorted(l)][-3:]
        m=[1,2,3][-len(l):]
        s+=sum(a*b for a,b in zip(l,m))
    return s

def size(sp,st):
    return len(sp) + sum(map(len,st.values()))

def run(tr):
    sp={(0,1):0}
    st={}
    for Y in range(1,101):
        # print('y',Y)
#        print(st,sp)
        #grow
        next={}
        for (x,y),i in sp.items():
            a,b,c=tr[i]
            n=(x-1,y,a),(x+1,y,b),(x,y+1,c)
            for dx,dy,v in n:
                if v>=0:
                    if dy not in st.get(dx,set()):
                        next[(dx,dy)] = max(next.get((dx,dy),-1),v)
            st[x]=st.get(x,set())|{y}
        sp=next
        #energy
        if Y>=5:
            E=calc_E(st)
            e_needed = 3 * size(sp,st)
#            print(E,e_needed)
            if E<e_needed:break

    return size(sp,st)


SUM=0
for tr in trees:
#    print(tr)
#    print()
    SUM+=run(tr)

print(SUM)


# ---
def other_t(trs,i):
    all_t=set()
    for I,(tr,sp,st) in trs.items():
        if I==i:pass
        all_t |= {*sp.keys()}
        all_t |= {(x,y)for x in st for y in st[x]}
    return all_t

def other_st(trs,i):
    all_t={}
    for I,(tr,sp,st) in trs.items():
        if I==i:break
        for x in st:
            all_t[x]=all_t.get(x,set())|st[x]
    return all_t

def calc_E2(st,trs,i):
    s=0
    L=other_st(trs,i)
    for x,l in st.items():
        a={*l, *L.get(x,set())}
        l=[[v in l,min(10,v)]for v in sorted(a)][-3:]
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

def run2(trees):
    trs = {}
    for i,tr in enumerate(trees):
        sp={(i*10,1):0}
        st={}
        trs[i]=[tr,sp,st]
        
    all_st={}
    dead=set()
    total = 0
    for Y in range(1,101):
#        print('y',Y,dead)
#        if len(dead)==len(trs):break
        for I,(tr,sp,st) in sorted(trs.items()):
            if I in dead:
                continue
#            print(I, tr, st,sp)
#            print(other_t(trs,I))
            #grow
            next={}
            for (x,y),i in sp.items():
                a,b,c=tr[i]
                n=(x-1,y,a),(x+1,y,b),(x,y+1,c)
                for dx,dy,v in n:
                    if v>=0:
                        if (dx,dy) not in other_t(trs,I) and dy not in st.get(dx,set()):
                            next[(dx,dy)] = max(next.get((dx,dy),-1),v)
                st[x]=st.get(x,set())|{y}
                all_st[x]=all_st.get(x,set())|{y}
            trs[I][1]=next
            #energy
            if Y>=5:
                E=calc_E2(st,trs,I)
                #E=calc_E(st)
                e_needed = 3 * size(sp,st)
#                print('  ',I,E,e_needed)
                if E<e_needed:
                    dead|={I}
    for I,(tr,sp,st) in trs.items():
        total += size(sp,st)
    
    print(total)
    print_trees(trs)
    return total


print(run2(trees))

#wrong
7110
7160
7335
7415
7468
7473
11008
14229
