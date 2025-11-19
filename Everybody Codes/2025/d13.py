DAY,_,_=__file__.rpartition('.')

def f(n,p):
    r=[]

    with open(f'{DAY}{p}.txt','r')as F:
        for l in F:
            l=l.rstrip('\n')
            l=[*map(int,l.split('-'))]
            l = l if len(l)>1 else l*2
            r+=[l]

    d=[1]
    for x,y in r[::2]:
        d+=[*range(x,y+1)]
    for x,y in r[1::2][::-1]:
        d+=[*range(x,y+1)][::-1]

    print(d[n%len(d)])

## --

f(2025,'a')

f(20252025,'b')

f(202520252025,'c')
