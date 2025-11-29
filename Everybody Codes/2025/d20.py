DAY,_,_=__file__.rpartition('.')

from collections import defaultdict

## ---

def solve(part):
    r=[]

    with open(f'{DAY}{part}.txt','r')as F:
        for l in F:
            l=l.rstrip('\n')
            r+=[l]
                    
    W,H=len(r[0]),len(r)

    def trans(x,y):
        return H-(y+x)//2-1-(y+x)%2,(W-y)//2-(y*x)%2+x+-~x//2

    numMoves=0
    e=defaultdict(lambda:[])
    for i in range(H):
        for j in range(W):
            x=r[i][j]
            if x=='S':
                xs,ys=i,j
            if x=='E':
                xe,ye=i,j
            if x in 'SET':
                moves = [(0,-1),(0,1)]
                if part=='c':moves += (0,0),
                if i%2==j%2:moves += (-1,0),
                else: moves += (1,0),
                
                for dx,dy in moves:
                    X,Y=i+dx,j+dy
                    if 0<=X<len(r) and 0<=Y<len(r[0]) and r[X][Y]!='.':
                        if part=='c':
                            X,Y=trans(X,Y)
                        y=r[X][Y]
                        if y in 'SET':
                            e[(i,j)]+=(X,Y),
                            numMoves+=1

    if part=='a':
        print(numMoves//2)
        return
    
    q=[[xs,ys,0]]
    s=set()
    for x,y,m in q:
        if (x,y) in s:
            continue
        if (x,y)==(xe,ye):
            print(m)
            return
        s|={(x,y)}
        for X,Y in e[(x,y)]:
            if (X,Y) not in s:
                q+=[X,Y,m+1],

## ---
solve('a')
solve('b')
solve('c')