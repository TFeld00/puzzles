DAY,_,_=__file__.rpartition('.')

def run(part):
    d={}
    n=[]

    with open(f'{DAY}{part}.txt','r')as F:
        for l in F:
            l=l.rstrip('\n')
            a,*l,_=[v.split('=')[1].split()for v in l.split(', ')]
            a=int(a[0])
            l=[set(v)for v in l]
            d[a]=l
            n+=[[a,*l]]
            
    def order(R):
        if not R:return[]
        i,l,r=R
        if i==0:return[]
        return order(l)+[i]+order(r)

    def order2(R):
        if not R:return[]
        i,l,r=R
        if i==0:return[]
        return [[i,1]]+order2(l)+[[i,2]]+order2(r)

    D={}
    def insert(v,p,n):
        o=order2(R)*2
        if n in o:o=o[o.index(n)+1:]
        for i,s in o:
            l = D[i][s]
            x = d[i][s]
            if not l:
                if (part=='a' and x==p) or x & p:
                    D[i][s]=D[v]
                    return
            elif part=='c':
                vl = l[0]
                pl = d[vl][0]
                if pl!=x and x==p:
                    D[i][s]=D[v]
                    return insert(vl,pl,order2(D[v])[-1])
        
    R=D[1]=[1,[],[]]
    for v,p,*_ in n[1:]:
        D[v]=[v,[],[]]
        insert(v,p,0)

    o=(order(R))
    print(sum(i*v for i,v in enumerate(o,1)))

run('a')
run('b')
run('c')