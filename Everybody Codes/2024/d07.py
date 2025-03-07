DAY,_,_=__file__.rpartition('.')

from itertools import permutations
import re
r=[]
s=0
t=''

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,*c=re.split(':|,',l)
        r+=[a,(c*10)[:10]],
        

l=[]
for a,c in r:
    p=10
    s=0
    for v in c:
        if v=='-':p-=1
        elif v=='+':p+=1
        s+=p
    l+=[s,a],

print(''.join(a for s,a in sorted(l,reverse=True)))


# ------------ Part 2 ------------

track = """S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-""".splitlines()


t=track[0]
for c in track[1:-1]:
    t+=c[-1]
t+=track[-1][::-1]
for c in track[1:-1][::-1]:
    t+=c[0]

t=t[1:]+t[:1]
    
L=len(t)*10
r=[]
with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,*c=re.split(':|,',l)
        r+=[a,(c*L)[:L]],

        
l=[]
for a,c in r:
    p=10
    s=0
    for w,v in zip(t*10,c):
        if w=='+':p+=1
        elif w=='-':p-=1
        elif v=='-':p-=1
        elif v=='+':p+=1
        s+=p
#        print(p,end=' ')
    l+=[s,a],
#    print()

print(''.join(a for s,a in sorted(l,reverse=True)))


# ------------ Part 3- -------------

r=[]
with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,*c=re.split(':|,',l)
        r+=[a,c],

track="""S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=       
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =          
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-""".splitlines()

t='S'
x=y=0
seen={(x,y)}
while 1:
    for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
        X,Y=x+dx,y+dy
        if (X,Y) in seen:continue
        if X<0 or X>=len(track[0]) or Y<0 or Y>= len(track):continue
        if track[Y][X]!=' ':break
    if track[Y][X]=='S':break
    t+=track[Y][X]
    seen|={(X,Y)}
    x,y=X,Y
t=t[::-1]


def run(c):
    p=10
    s=0
    for w,v in zip(t*11,c*340):
        if w=='+':p+=1
        elif w=='-':p-=1
        elif v=='-':p-=1
        elif v=='+':p+=1
        s+=p
    return s

rival = run(r[0][1])

res=0
for c in set(permutations((*'+++++---===',))):
    s=run(c)
    if s>rival:res+=1

print(res)