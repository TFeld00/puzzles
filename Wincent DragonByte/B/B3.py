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
    divs = [v for v in range(3,int(n**0.5)+1) if n%v==0 or (n-1)%v==0] + [n-1]
    for b in divs:
        m=n
        while m>0:
            a=m%b
            m//=b
            if a>1:break
        if a<2 and m==0:
            res+=str(b)+'\n',
            print(b)
            break

with open(f'{PROB}.out','w', encoding='utf8')as F:
    F.writelines(res)