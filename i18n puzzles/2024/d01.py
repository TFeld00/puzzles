DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
s=0

for l in r:
    a,b=len(l),len(bytes(l,'utf-8'))
    s+=[0,7,11,13][(a<=140)+(b<=160)*2]
print(s)
