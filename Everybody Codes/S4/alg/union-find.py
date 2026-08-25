

P={}
S={}
def find(x):
    while P[x] and P[x]!=x:
        P[x]=P[P[x]]
        x=P[x]
    return x

def union(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        if S[x]<S[y]:
            x,y=y,x
    P[y]=x
    S[x]+=S[y]

INIT=[]
for v in INIT:
    P[v]=v
    S[v]=1
