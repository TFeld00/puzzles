DAY,_,_=__file__.rpartition('.')

r=[]
with open(f'{DAY}.txt', 'r') as F:
    for l in F:
        l=l.rstrip('\n')
        r+=list(l),

def solve(r,turn=0):
    s=set()
    x,y=0,0
    while 1:
        c=r[y][x]
        if (x,y)in s:
            if turn and 0<x<len(r[0])-1 and 0<y<len(r)-1:
                x,y = [(x,y-1),(x+1,y),(x,y+1),(x-1,y)]['<^>v'.find(c)]
                turn-=1
                continue
            elif turn:
                pass
            else:
                break
        s|={(x,y)}
        x,y = [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]['<^>v'.find(c)]
        c=r[y][x]
    return len(s)

# ---

print(solve(r))

# ---

l=[]
for i in range(1,len(r)-1):
    for j in range(1,len(r[i])-1):
        C=r[i][j]
        for c in '<>^v':
            r[i][j]=c
            l+=solve(r),
            r[i][j]=C

print(max(l))

# ---

l=[]
for i in range(1,len(r)-1):
    for j in range(1,len(r[i])-1):
        C=r[i][j]
        for c in '<>^v':
            r[i][j]=c
            l+=solve(r,3),
            r[i][j]=C

print(max(l))

