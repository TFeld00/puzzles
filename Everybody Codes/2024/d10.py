DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers

COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
}


def runes(r,I=2,J=2):
    cols = [set(l[I-2:I+6])-{'.'}for l in zip(*r)]
    rows = [set(l[J-2:J+6])-{'.'}for l in r]
    undo = {}
    for i in range(I,I+4):
        l=r[i]
        for j in range(J,J+4):
            c=l[j]
            undo[(i,j)]=c
            if c=='.':
                s=(cols[j]&rows[i])
                if s:
                    c2=s.pop()
                    r[i][j] = c2
                    cols[j]-={c2}
                    rows[i]-={c2}
    for i in range(I,I+4):
        l=r[i]
        for j in range(J,J+4):
            c=l[j]
            if c=='.':
                if len(rows[i])==1 and '?'in cols[j]:
                    c2 =rows[i].pop()
                    for di in range(I-2,I+6):
                        if r[di][j]=='?':
                            undo[(di,j)]='?'
                            r[di][j]=c2
                    r[i][j] = c2
                elif len(cols[j])==1 and '?'in rows[i]:
                    c2 =cols[j].pop()
                    for dj in range(J-2,J+6):
                        if r[i][dj]=='?':
                            undo[(i,dj)]='?'
                            r[i][dj]=c2
                    r[i][j] = c2
    
    s=''
    for i in range(I,I+4):
        l=r[i]
        for j in range(J,J+4):
            s+=l[j]
    if '.' in s:
        for (i,j),c in undo.items():
            r[i][j]=c
    return s

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=list(l)
        r+=[l]

print(runes(r))


r=[]
s=0

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l.split()]

for x in parse_no_headers(r):
    for v in zip(*x):
        v=[list(l)for l in v]
        res = runes(v)
        s+= sum(i*(ord(c)-64) for i,c in enumerate(res,1))
print(s)


r=[]
s=0

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=list(l)
        r+=[l]

R=[]
for i in range(0,len(r)-2,6):
    rows = r[i:i+8]
    for j in range(0,len(r[0])-2,6):
        R+=(i,j),

D={}
for _ in range(2):
    for i,j in R:
        res = runes(r,i+2,j+2)
        D[(i,j)]=res
        
for res in D.values():
    if '.' in res:continue
    s+= sum(i*(ord(c)-64) for i,c in enumerate(res,1))
print(s)