DAY,_,_=__file__.rpartition('.')
r=[]

with open(f'{DAY}.txt', 'r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
print(sum(l[(i*2)%len(l)]=='💩' for i,l in enumerate(r)))
