DAY,_,_=__file__.rpartition('.')

from math import *

for part in 'ab':
    r=[]
    with open(f'{DAY}{part}.txt','r')as F:
        for l in F:
            l=l.rstrip('\n')
            l=l.split(', ')
            x=[]
            for v in l:
                a,b=v.split('=')
                if a=='connections':b=b.split(',')
                x+=b,
            r+=[x]

    d={}
    E={}
    for i,e,o in r:
        d[i]=o
        E[i]=int(e)

    i=max(r,key=lambda v:len(v[2]))[0]

    e=5 if part =='a' else 10
    q={i:1}
    while e:
        nq={}
        for i,v in q.items():
            E[i]+=e*v
            for o in d[i]:
                nq[o]=nq.get(o,0)+v
        e-=1
        q=nq

    print(sum(E.values()))


# -----------


for part in 'c': # works for all three parts
    r=[]
    with open(f'{DAY}{part}.txt','r')as F:
        for l in F:
            l=l.rstrip('\n')
            l=l.split(', ')
            x=[]
            for v in l:
                a,b=v.split('=')
                if a=='connections':b=b.split(',')
                x+=b,
            r+=[x]

    def f(i, init = 10, limit=inf):
        dead=set()
        E={}
        d={}
        for j,e,o in r:
            d[j]=set(o)
            E[j]=int(e)
        e=init
        q={(i,e):1}
        while q:
            nq={}
            for (i,e),v in q.items(): # propagate
                if i in dead:continue
                E[i]+=e*v
                if e>1:
                    for o in d[i]:
                        nq[(o,e-1)]=nq.get((o,e-1),0)+v
            for (i,e),v in q.items(): # explosion
                if i in dead:continue
                if E[i]>=limit:
                    dead.add(i)
                    E[i]=0
                    for w in d.values():w-={i}
                    for o in d[i]:
                        nq[(o,10)]=nq.get((o,10),0)+1
            q=nq
        return sum(E.values())


    init = 5 if part == 'a' else 10
    if part in 'ab':
        i=max(r,key=lambda v:len(v[2]))[0]
        print(f(i,init))
    else:
        limit = 1000000
        print(max(f(i,init,limit) for i,*_ in r))
