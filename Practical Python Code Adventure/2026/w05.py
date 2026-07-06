DAY,_,_=__file__.rpartition('.')

r=[]
with open(f'{DAY}.1.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=l,

res=[0]*7
d={
    (0,0,0,0): 0,
    (0,0,1,1): 1,
    (1,1,0,0): 2,
    (1,0,0,1): 3,
    (0,1,0,1): 4,
    (0,1,1,0): 5,
    (1,0,1,0): 6
}
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='7':
            U=int(r[i-1][j] in '245')
            D=int(r[i+1][j] in '236')
            L=int(r[i][j-1] in '134')
            R=int(r[i][j+1] in '156')

            res[d[(U,D,L,R)]]+=1

print(''.join(map(str,res[1:])))
# ---

r=[]
i=0
with open(f'{DAY}.2.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=list(l),
        if '@'in l:
            x,y=l.find('@'),i
        i+=1

w=1
q=[(x,y)]
for x,y in q:
    for dx in (-1,0,1):
        for dy in (-1,0,1):
            if [dx,dy]!=[0,0]:
                X,Y=x+dx,y+dy
                if len(r)>Y>=0<=X<len(r[0])and r[Y][X]=='0':
                    w+=1
                    r[Y][X]='w'
                    q+=(X,Y),
print(w)