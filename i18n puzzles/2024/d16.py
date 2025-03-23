DAY,_,_=__file__.rpartition('.')

r=[]
t=''

with open(f'{DAY}.txt', 'r', encoding='cp437')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        t+=l
        

if 'Start' in t:
    r=[l[7:-7] for l in r[5:-6]]

def f(c):
    if c=='─':return (0,1,0,1)
    if c=='│':return (1,0,1,0)
    if c=='┌':return (0,1,1,0)
    if c=='┐':return (0,0,1,1)
    if c=='└':return (1,1,0,0)
    if c=='┘':return (1,0,0,1)
    if c=='├':return (1,1,1,0)
    if c=='┤':return (1,0,1,1)
    if c=='┬':return (0,1,1,1)
    if c=='┴':return (1,1,0,1)
    if c=='═':return (0,2,0,2)
    if c=='║':return (2,0,2,0)
    if c=='╔':return (0,2,2,0)
    if c=='╗':return (0,0,2,2)
    if c=='╚':return (2,2,0,0)
    if c=='╝':return (2,0,0,2)
    if c=='╞':return (1,2,1,0)
    if c=='╠':return (2,2,2,0)
    if c=='╡':return (1,0,1,2)
    if c=='╣':return (2,0,2,2)
    if c=='╤':return (0,2,1,2)
    if c=='╥':return (0,1,2,1)
    if c=='╦':return (0,2,2,2)
    if c=='╧':return (1,2,0,2)
    if c=='╨':return (2,1,0,1)
    if c=='╪':return (1,2,1,2)
    if c=='╫':return (2,1,2,1)
    return (0,0,0,0)
    

w=len(r[0])
r=[[*map(f,' '+l+' ')]for l in r]
r=[[(0,0,0,0),(1,0,1,0),*[(0,0,0,0)]*w]]+r+[[*[(0,0,0,0)]*w,(1,0,1,0),(0,0,0,0)]]

d={}
for c in '─│┌┐└┘├┤┬┴═║╔╗╚╝╞╠╡╣╤╥╦╧╨╪╫ ':
    d[f(c)]=c

for l in r:print(''.join(d[c]for c in l))

init = [l[:]for l in r[:]]

def diff(r1,r2):
    s=0
    for l1,l2 in zip(r1,r2):
        for c1,c2 in zip(l1,l2):
            for i in 0,1,2,3:
                a=c1[i:]+c1[:i]
                if a==c2:
                    s+=i
                    break
    return s

H=len(r)-1
W=w+1
def solve(r,i=1,j=1):
    if j==W:
        j=1;i+=1
    if i==H:
        for l in r:print(''.join(d.get(tuple(c),'x')for c in l))
        print(diff(r,init))
        exit(0)
    a=r[i][j]
    if sum(a)==0:
        solve(r,i,j+1)
    else:
        moves=set()
        for t in 0,1,2,3:
            x=a[t:]+a[:t]
            moves|={x}
        for x in moves:
            u=r[i-1][j]
            l=r[i][j-1]
            if x[0]==u[2] and x[3]==l[1]:
                r[i][j]=x
                solve(r,i,j+1)
                r[i][j]=a
    
solve(r)