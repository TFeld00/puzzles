PROB,_,_=__file__.rpartition('.')
r=[]

with open(f'{PROB}.in','r', encoding='utf8')as F:
    for l in F:
        l=int(l)
        r+=[l]
        
_,*r=r

res = []

for n in r:
    b=3
    if n==2:
        res+='-1\n',
        continue
    if n<4:
        res+='%d\n'%n,
        continue
    #divs = [v for v in range(3,int(n**0.5)+1) if n%v<1 and (n//v)%v<2] + [n-1]
    b=3
    r=1
    for b in range(3,int(n**0.5)+1):
        m=n
        while m>0:
            a=m%b
            m//=b
            if a>1:break
        if a<2:
            res+=str(b)+'\n',
            r=0
            break
    if r:
        res+=str(n-1)+'\n',

with open(f'{PROB}.out','w', encoding='utf8')as F:
    F.writelines(res)