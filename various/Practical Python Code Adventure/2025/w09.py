DAY,_,_=__file__.rpartition('.')

r=[]
with open(f'{DAY}.1.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=l,


# ---

r=[]
with open(f'{DAY}.2.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=l,
