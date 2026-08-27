DAY,_,_=__file__.rpartition('.')

r=[]
s=0
t=''

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split('=')
        r+=[l]
        
w,h,ho,vo=[x[1]for x in r]
w=int(w)
h=int(h)
m=[[0]*w for _ in range(h)]

for i in range(h+1):
    c=ho[i%len(ho)]
    for j in range(int(c),w,2):
        a=i
        if a<h:
            m[a][j]|=1
        a=i-1
        if 0<=a<h:
            m[a][j]|=2

for j in range(w+1):
    c=vo[j%len(vo)]
    for i in range(int(c),h,2):
        a=j
        if a<w:
            m[i][a]|=4
        a=j-1
        if 0<=a<w:
            m[i][a]|=8

print(sum(l.count(15)for l in m))

# ---

r=[]
s=0
t=''

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split('=')
        r+=[l]

w,h,ho,vo=[x[1]for x in r]
w=int(w)
h=int(h)
m=[[0]*w for _ in range(h)]

for i in range(h+1):
    c=ho[i%len(ho)]
    for j in range(int(c),w,2):
        a=i
        if a<h:
            m[a][j]|=1
        a=i-1
        if 0<=a<h:
            m[a][j]|=2

for j in range(w+1):
    c=vo[j%len(vo)]
    for i in range(int(c),h,2):
        a=j
        if a<w:
            m[i][a]|=4
        a=j-1
        if 0<=a<w:
            m[i][a]|=8

c=0
for i in range(h):
    if i:
        c=m[i-1][0]&16
    if i and m[i][0]&1:
        c^=16
    for j in range(w):
        if j and m[i][j]&4:
            c^=16
        m[i][j]|=c

print(max(sum(l.count(15|16)for l in m),sum(l.count(15)for l in m)))

# ---

r=[]
s=0
t=''

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split('=')
        r+=[l]
        

w,h,ho,vo=[x[1]for x in r]
w=int(w)
h=int(h)

a,b=len(ho),h%len(ho)
c,d=len(vo),w%len(vo)

H,W=a+a,c+c
m=[[0]*(W) for _ in range(H)]

for i in range(H+1):
    c=ho[i%len(ho)]
    for j in range(int(c),W,2):
        a=i
        if a<H:
            m[a][j]|=1
        a=i-1
        if 0<=a<H:
            m[a][j]|=2

for j in range(W+1):
    c=vo[j%len(vo)]
    for i in range(int(c),H,2):
        a=j
        if a<W:
            m[i][a]|=4
        a=j-1
        if 0<=a<W:
            m[i][a]|=8

c=0
for i in range(H):
    if i:
        c=m[i-1][0]&16
    if i and m[i][0]&1:
        c^=16
    for j in range(W):
        if j and m[i][j]&4:
            c^=16
        m[i][j]|=c

A=15|16
x=sum(l.count(A)*(w//W) + l[:w%W].count(A) for l in m[:H])*(h//H) +sum(l.count(A)*(w//W) + l[:w%W].count(A) for l in m[:h%H])
A=15
y=sum(l.count(A)*(w//W) + l[:w%W].count(A) for l in m[:H])*(h//H) +sum(l.count(A)*(w//W) + l[:w%W].count(A) for l in m[:h%H])

print(max(x,y))