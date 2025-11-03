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

maxGcd = 10
maxDepth=0
digits={}

def getSets(l,taken=[], g=None):
    global maxGcd
    global maxDepth
    lt=len(taken)

    if lt<=2:print(taken)
    
    if taken:
        l={i:[v for v in ll if all(a!=b for a,b in zip(digits[v],digits[taken[-1]]))]for i,ll in l.items()if i>=lt}

        if lt<=3:
            ra = digits[taken[0]] if lt>0 else None
            rb = digits[taken[1]] if lt>1 else None
            rc = digits[taken[2]] if lt>2 else None
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

        elif lt<=6:
            rg = digits[taken[3]] if lt>3 else None
            rh = digits[taken[4]] if lt>4 else None
            ri = digits[taken[5]] if lt>5 else None
                
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

        else:
            rd = digits[taken[6]] if lt>6 else None
            rf = digits[taken[7]] if lt>7 else None
            re = digits[taken[8]] if lt>8 else None
                
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

        if lt==9:
            if g>maxGcd:print(g)
            maxGcd=max(g,maxGcd)
            yield taken
            return


    for x in l[lt]:
        g2=gcd(g or x,x)
        if g2< maxGcd:continue
        
        yield from getSets(l,taken+[x],g2)

digits={}

res={}
l={}

for skip in range(10):
    if skip in [0,2,5]:continue
    maxDepth=0
    l={i:[] for i in range(9)}

    for v in permutations({*range(10)}-{skip}):
        x=0
        for c in v:
            x=x*10+c
        digits[x]=v

        for i,row in enumerate(initial_grid):
            if all(b==None or a==b for a,b in zip(v,initial_grid[i])) and all(all(a!=b for a,b in zip(v,row))for row in initial_grid[:i]+initial_grid[i+1:]):
                l[i]+=x,
    print(skip,[len(v)for v in l.values()])
    for s in getSets(l):
        res[maxGcd] = res.get(maxGcd,[]) + [s]
        print(s,maxGcd)
#        break
#        exit(0)
#    print(skip)
print(maxGcd)
print(len(res[maxGcd]))