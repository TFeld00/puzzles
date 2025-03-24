DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
from img.img import read_img, write_img, write_img_fromlist     #write_img(DAY,COLS)

r=[]

with open(f'{DAY}.txt', 'r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        l=bytearray([int(''.join(v),16)for v in zip(*[iter(l)]*2)])
        r+=[l]

r = parse_no_headers(r)

W=0
for p in r:
    try:
        s=p[0].decode('utf8')
        if '═' in s:W+=len(p[0])
    except:
        pass
H=0
for p in r:
    x=0
    for l in p:
        try:
            s=l[:1].decode('utf8')
            x |= s.startswith('|')
        except:
            pass
    if x:H+=len(p)

M=[bytearray([0xff]*W) for _ in range(H)]

used=[]

TLH=BLH=0
for p in r:
    try:
        s=p[0].decode('utf8')
        if s.startswith('╔'):
            for i,l in enumerate(p):
                M[i][0:len(l)]=l
            TLH=len(p)
            used+=[p]
        if s.endswith('╗'):
            for i,l in enumerate(p):
                M[i][-len(l):]=l
            used+=[p]
    except:pass
    try:
        s=p[-1].decode('utf8')
        if s.startswith('╚'):
            for i,l in enumerate(p):
                M[H-len(p)+i][0:len(l)]=l
            used+=[p]
            BLH=len(p)
        if s.endswith('╝'):
            for i,l in enumerate(p):
                M[H-len(p)+i][-len(l):]=l
            used+=[p]
    except:pass

top=[]
bottom=[]
left=[]
right=[]
for p in r:
    if p in used:continue
    try:
        s=p[0].decode('utf8')
        if '═-' in s:top+=p,
    except:
        pass
    try:
        s=p[-1].decode('utf8')
        if '═-' in s:bottom+=p,
    except:
        pass
for p in r:
    x=0
    for l in p:
        try:
            s=l[:1].decode('utf8')
            x |= s.startswith('|')
        except:
            pass
    if x:left+=p,
for p in r:
    x=0
    for l in p:
        try:
            s=l[-1:].decode('utf8')
            x |= s=='|'
        except:
            pass
    if x:right+=p,

def valid(M,j,i0,i1):
    try:
        x=0
        a=[]
        for i in range(i0,i1):
            ra = range(j+32,j,-1)
            for k in ra:
                if 0xff in M[i][:j+16]:x+=1;break
                try:
                    s=M[i][:k].decode('utf8')
                    x+=1
                    a+=s,
                    break
                except:pass
        return x==i1-i0
    except:
        return False

def solveTop(M,j,used):
    if len(used)==len(top):
        try:
            x=0
            for i in range(TLH):
                if 0xff in M[i]:x+=1;continue
                s=M[i].decode('utf8')
                x+=1
            if x==TLH:
                print('found top!')
                return 1
        except:
            pass
    for p in top:
        if p in used:continue
        for i,l in enumerate(p):
            M[i][j:j+len(l)]=l[:]
        if valid(M,j,0,TLH):
            a=solveTop(M,j+16,used+[p])
            if a:return a
        for i,l in enumerate(p):
            M[i][j:j+len(l)]=[0xff]*len(l)

def solveBottom(M,j,used):
    if len(used)==len(bottom):
        try:
            x=0
            for i in range(H-BLH,H):
                if 0xff in M[i]:x+=1;continue
                s=M[i].decode('utf8')
                x+=1
            if x==BLH:
                print('found bottom!')
                return 1
        except:
            pass
    for p in bottom:
        if p in used:continue
        for i,l in enumerate(p,H-len(p)):
            M[i][j:j+len(l)]=l[:]
        if valid(M,j,H-BLH,H):
            a=solveBottom(M,j+16,used+[p])
            if a:return a
        for i,l in enumerate(p,H-len(p)):
            M[i][j:j+len(l)]=[0xff]*len(l)

rest = []
for p in r:
    if p not in top+bottom+left+right:
        rest+=p,

def next(M):
    for i,l in enumerate(M):
        if 0xff in l:
            j=l.index(0xff)
            return i,j

def solve(M,used):
    n=next(M)
    if not n:
        print('done!')
        return 1
    i,j=n
    pieces = rest
    if j==0:pieces = left
    elif j==W-16:pieces = right

    for p in pieces:
        if p in used:continue
        if i+len(p)>H:continue
        possible = 1
        for pi,l in enumerate(p,i):
            if any(c!=0xff for c in M[pi][j:j+len(l)]):possible = 0
        if not possible:continue

        for pi,l in enumerate(p,i):
            M[pi][j:j+len(l)]=l[:]
        if valid(M,j,i,i+len(p)):
            a=solve(M,used+[p])
            if a:return a
        for pi,l in enumerate(p,i):
            M[pi][j:j+len(l)]=[0xff]*len(l)


solveTop(M,16,[])
solveBottom(M,16,[])
solve(M,[])

I=J=0
RES=[]
with open(f'{DAY}o.txt', 'w', encoding='utf8')as F:
    for l in M:
        s=l.decode('utf8')
        F.write(s+'\n')
        if '╳' in s:
            J=s.index('╳')
            print(I*J)
        I+=1
        RES+=s,

with open(f'{DAY}b.txt', 'w', encoding='utf8')as F:
    for l in M:
        F.write(''.join('%02x'%c for c in l)+'\n')

S=set(c for l in RES for c in l)
COLS = {}
m=int(255/len(S))
for i,c in enumerate('o¨ñ^╳═≋∧∨𐲣•-I¦𐌉⁖※𐌡𐧸𐳓∞¯║╚|:╔∣±𐌘Δ╝~¤∅8−Ø𐳻𐌟ŵ#𑀍φ.v╗𐀏'):
    i*=m
    COLS[c]=(i,i,i)
COLS['╳']=(255,0,0)

write_img_fromlist(RES,f'{DAY}',COLS)
