DAY,_,_=__file__.rpartition('.')

from decimal import *
PI='31415926535897932384626433832795'

def shift(c,n):
    v=ord(c)%32-1
    v= (v-n)%26
    v += ord('A') if c.isupper() else ord('a')
    return chr(v)

r=None
M=[]
N={}
with open(f'{DAY}_1.txt','r')as F:
    F.readline()
    for l in F:
        a,b,c=l.split()
        if b.replace('.','')in PI:
            if r==None:
                r=Decimal(b)
            elif int(a)%2:
                r/=Decimal(b)
            else:
                r*=Decimal(b)

            M+=[int(b.replace('.','')),c],
        else:
            N[c]=int(a),int(b.replace('.',''))

print(str(r).replace('.','')[:10])

R=[]
with open(f'{DAY}_2.txt','r')as F:
    for l in F:
        R+=l.split()

def shift(c,n):
    v=ord(c)%32-1
    v= (v+n)%26
    v += ord('A') if c.isupper() else ord('a')
    return chr(v)

X=[]
for s,t in M:
    t=''.join(shift(c,s)for c in t)
    X+=N[t],
RES=''
for _,v in sorted(X):
    RES+=R[v%len(R)]
print(RES)