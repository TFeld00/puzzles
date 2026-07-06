DAY,_,_=__file__.rpartition('.')

from functools import cache

r=[]
with open(f'{DAY}.1.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=l,
R=[]
for l in r[1:]:
    c,b,o,w,x=l.split(',')
    R+=(c,b,o,int(w),int(x)),


@cache
def f1(i,w):
    if w<0:return -1e9
    if w==0 or not R[i:]:
        return 0
    *_,v,x=R[i]
    a=f1(i+1,w)
    if w>=v:
        return max(a, f1(i+1,w-v)+x)
    return a
    
print(f1(0,300))

# ---

roasts = {v:1<<i for i,v in enumerate({v for _,_,v,_,_ in R})}
beans = {v:1<<i for i,v in enumerate({v for _,v,_,_,_ in R})}
all_roasts = (2**len(roasts))-1

@cache
def f2(i,b_used,r_used,w):
    if w<0:return -1e9
    if w==0 or not R[i:]:
        if r_used==all_roasts:
            return 0
        return -1e9
    _,b,r,v,x=R[i]
    b=beans[b]
    r=roasts[r]
    a=f2(i+1,b_used,r_used,w)
    if w>=v and b_used&b==0:
        return max(a, f2(i+1,b_used | b,r_used | r,w-v)+x)
    return a
    
print(f2(0,0,0,300))