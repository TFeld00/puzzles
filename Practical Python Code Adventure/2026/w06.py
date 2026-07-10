DAY,_,_=__file__.rpartition('.')

def angle(p,q,r):
    """Determines the orientation of triplet (p, q, r).
    Returns:
        > 0 if Counter-Clockwise (Left turn)
        < 0 if Clockwise (Right turn)
        = 0 if Collinear
    """
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

def find_hull(r):
    s=sorted(r)
    h=[]
    e=None
    p=s[0]
    while 1:
        h+=p,
        e=s[0]
        for v in s:
            if e==p or angle(p,e,v)>0:
                e=v
        p=e
        if e==h[0]:break
    return h

def inside_hull(point, h):
    for a,b in zip(h,h[1:]+h[:1]):
        if angle(a, b, point) > 0:
            return False            
    return True

# ---

r=[]
with open(f'{DAY}.1.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[*map(int,l.split(','))],


h=find_hull(r)

print(len(h)*len(r))

# ---

r=[]
with open(f'{DAY}.2.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        a,b,c=l.split(',')
        r+=(int(a),int(b),c),


h=find_hull([v for v in r if v[2]!='U'])
out = [v for v in r if v[2]=='U' and not inside_hull(v,h)]

print(len(h)*(len(r)-len(out)))
