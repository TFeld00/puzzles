from queue import Queue


r=[]
r="""......#..
.#......#
#.####...
.#....#..
##..#.#.#
#..#.....
#......#.
.#..#.##.""".split()


def bfs(r,x,y):
    W=len(r[0])
    H=len(r)
    q=Queue()
    s=set()
    q.put((x,y,0))
    while not q.empty():
        x,y,l=q.get()
        
        if (x,y)==(W-1,H-1):
            print(l)
            #WIN
            return l
        
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            X,Y=x+dx,y+dy
            if (X,Y)in s:continue

            s|={(X,Y)}
            if 0<=X<W and 0<=Y<H:
                if r[Y][X]=='.':
                    q.put((X,Y,l+1))