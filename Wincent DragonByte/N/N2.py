PROB,_,_=__file__.rpartition('.')
r=[]

with open(f'{PROB}.in','r', encoding='utf8')as F:
    for l in F:
        l=int(l)
        r+=[l]
        
_,*r=r

res = []

for n in r:
    v=1
    for i in range(1,n*10):
        j=i+n
        if sum(map(int,str(i)))==sum(map(int,str(j))):
            res+='%d %d\n'%(i,j)
            v=0
            break
    if v:
        res +='NONE\n'

with open(f'{PROB}.out','w', encoding='utf8')as F:
    F.writelines(res)