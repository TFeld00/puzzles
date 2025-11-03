from sudoku import solveSudoku

X = None
initial_grid = [
    [X, X, X, X, X, X, X, 2, X],
    [X, X, X, X, 2, X, X, X, 5],
    [X, 2, X, X, X, X, X, X, X],
    [X, X, 0, X, X, X, X, X, X],
    [X, X, X, X, X, X, X, X, X],
    [X, X, X, 2, X, X, X, X, X],
    [X, X, X, X, 0, X, X, X, X],
    [X, X, X, X, X, 2, X, X, X],
    [X, X, X, X, X, X, 5, X, X],
]

digits = [*range(10)]
alphabet = list(set(v for l in initial_grid for v in l) - {X})
alphabet += [chr(65+x) for x in range(6)]

from itertools import permutations, combinations
from math import gcd

maxGcd = 9

digits={}

def getSets(l,taken=[], g=None):
    global maxGcd
    if taken:
        l=[v for v in l if all(a!=b for a,b in zip(digits[v],digits[taken[-1]]))]
        if not any(digits[a][4]==2 and digits[a][8]==5 for a in l):return
        lt=len(taken)
        ra = taken[0] if lt>0 else None
        rb = taken[1] if lt>1 else None
        rc = taken[2] if lt>2 else None

        rg = taken[3] if lt>3 else None
        rh = taken[4] if lt>4 else None
        ri = taken[5] if lt>5 else None

        rd = taken[6] if lt>6 else None
        rf = taken[7] if lt>7 else None
        re = taken[8] if lt>8 else None

        if ra and rb:
            if {ra[:3]}&{rb[:3]}: return
            if {ra[3:6]}&{rb[3:6]}: return
            if {ra[6:9]}&{rb[6:9]}: return
        if ra and rc:
            if {ra[:3]}&{rc[:3]}: return
            if {ra[3:6]}&{rc[3:6]}: return
            if {ra[6:9]}&{rc[6:9]}: return
        if rc and rb:
            if {rc[:3]}&{rb[:3]}: return
            if {rc[3:6]}&{rb[3:6]}: return
            if {rc[6:9]}&{rb[6:9]}: return

            
        if rd and re:
            if {rd[:3]}&{re[:3]}: return
            if {rd[3:6]}&{re[3:6]}: return
            if {rd[6:9]}&{re[6:9]}: return
        if rd and rf:
            if {rd[:3]}&{rf[:3]}: return
            if {rd[3:6]}&{rf[3:6]}: return
            if {rd[6:9]}&{rf[6:9]}: return
        if rf and re:
            if {rf[:3]}&{re[:3]}: return
            if {rf[3:6]}&{re[3:6]}: return
            if {rf[6:9]}&{re[6:9]}: return

            
        if rg and rh:
            if {rg[:3]}&{rh[:3]}: return
            if {rg[3:6]}&{rh[3:6]}: return
            if {rg[6:9]}&{rh[6:9]}: return
        if rg and ri:
            if {rg[:3]}&{ri[:3]}: return
            if {rg[3:6]}&{ri[3:6]}: return
            if {rg[6:9]}&{ri[6:9]}: return
        if ri and rh:
            if {ri[:3]}&{rh[:3]}: return
            if {ri[3:6]}&{rh[3:6]}: return
            if {ri[6:9]}&{rh[6:9]}: return

        if len(taken)==9:
            if g>maxGcd:print(g)
            maxGcd=max(g,maxGcd)
            yield taken


    for i,x in enumerate(l[lt]):
        lt=len(taken)
        if lt==0 and digits[x][7]!=2:continue
        if lt==1 and (digits[x][4]!=2 or digits[x][8]!=5):continue
        if lt==2 and digits[x][1]!=2:continue
       
        if lt==3 and digits[x][4]!=0:continue
        if lt==4 and digits[x][5]!=2:continue
        if lt==5 and digits[x][6]!=5:continue
       
        if lt==6 and digits[x][2]!=0:continue
        if lt==7 and digits[x][3]!=2:continue
        g=gcd(g or x,x)
        if g< maxGcd:return
        
        yield from getSets(l,taken+[x],g)

digits={}

res={}

for skip in range(10):
    if skip in [0,2,5]:continue

    l=[]
    for v in permutations({*range(10)}-{skip}):
        x=0
        for c in v:
            x=x*10+c
        digits[x]=v
        l+=x,
    for s in getSets(l):
        res[maxGcd] = res.get(maxGcd,[]) + [s]
        print(s,maxGcd)
#        break
#        exit(0)
#    print(skip)
print(maxGcd)
print(len(res[maxGcd]))