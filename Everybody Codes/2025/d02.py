DAY,_,_=__file__.rpartition('.')

s=''
with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=l
        
a,b=eval(s[2:])

x=y=0
for _ in range(3):
    x,y= [x * x - y * y, x * y + y * x]
    x=int(x/10)
    y=int(y/10)
    x+=a
    y+=b
print(str([x,y]).replace(' ',''))

# -----------

s=''
with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=l        
        
def f(a,b):
    x=y=0
    for _ in range(100):
        x,y= [x * x - y * y, x * y + y * x]
        x=int(x/100000)
        y=int(y/100000)
        x+=a
        y+=b
        if x>1000000 or x< -1000000 or y>1000000  or y< -1000000 :
            return False
    return True

a,b=eval(s[2:])
t=0
for i in range(a,a+1001,10):
    for j in range(b,b+1001,10):
        t+=f(i,j)
print(t)


# -----------

s=''

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=l

a,b=eval(s[2:])
t=0
for i in range(a,a+1001,1):
    for j in range(b,b+1001,1):
        t+=f(i,j)
print(t)
