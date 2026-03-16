DAY,_,_=__file__.rpartition('.')

import re
from collections import defaultdict
import heapq

MORSE = {
        '.-': 'A', '-...': 'B', '-.-.': 'C',
        '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I',
        '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
        '-': 'T', '..-': 'U', '...-': 'V',
        '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
        '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
        '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'
    }

MORSE_2 = {b:a for a,b in MORSE.items()}


with open(f'{DAY}_morse.txt','r')as F:
    for l in F:
        r=''
        for v in re.split('( +)',l.rstrip()):
            if v=='   ':continue
            elif v in (' ',' '*4):r+=' '
            else:
                r+=MORSE.get(v,v)
        print(r)


# ----------------- Part 2 ------------------

GRID=[]
W=H=100

with open(f'{DAY}_pi.txt','r')as F:
    r=''
    for l in F:
        for c in l:
            if c.isdigit():r+=c
            if len(r)==W:
                GRID+=r,
                r=''
            if len(GRID)==H:
                break

def cost(v):
    x=MORSE_2[v]
    return x.count('-')*3 + x.count('.') + int(v)

M =[
    [cost(v)for v in l] for l in GRID
]

def dijkstra(start,target):
    distances = defaultdict(lambda:[float('infinity'),0,None])
    x,y=start
    distances[start]=[M[y][x],1,None]
    pq=[(M[y][x],start)]
    
    while pq:
        d,(x,y) = heapq.heappop(pq)
        l=distances[(x,y)][1]
        if (x,y) == target:
            return d*l
        for dx,dy in (-1,0),(1,0),(0,-1),(0,1):
            X,Y=x+dx,y+dy
            if 0<=X<W and 0<=Y<H:
                c=M[Y][X]
                D=d+c
                Dprev,_,prev=distances[(X,Y)]
                if D<Dprev:
                    distances[(X,Y)]=[D,l+1,(x,y)]
                    heapq.heappush(pq, (D, (X,Y)))
                elif D==Dprev:
                    prevX,prevY=prev
                    dir1 = (prevX-X),(prevY-Y)
                    dir2 = -dx,-dy
                    d1,d2 = [[(1,0),(0,1),(-1,0),(0,-1)].index(v)for v in (dir1,dir2)]
                    if d2<d1:
                        distances[(X,Y)]=[D,l+1,(x,y)]
                        heapq.heappush(pq, (D, (X,Y)))


def dijkstra_normal(start,target):
    distances = defaultdict(lambda:[float('infinity'),0,None])
    x,y=start
    distances[start]=[M[y][x],1,None]
    pq=[(M[y][x],start)]
    
    while pq:
        d,(x,y) = heapq.heappop(pq)
        l=distances[(x,y)][1]
        if (x,y) == target:
            return d*l
        for dx,dy in (-1,0),(1,0),(0,-1),(0,1):
            X,Y=x+dx,y+dy
            if 0<=X<W and 0<=Y<H:
                c=M[Y][X]
                D=d+c
                Dprev,_,prev=distances[(X,Y)]
                if D<Dprev:
                    distances[(X,Y)]=[D,l+1,(x,y)]
                    heapq.heappush(pq, (D, (X,Y)))


print()
print(dijkstra((W-1,H-1),(0,0)))
#print(dijkstra_normal((W-1,H-1),(0,0)))
#print(dijkstra_normal((0,0),(W-1,H-1)))

