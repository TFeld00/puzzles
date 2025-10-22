import re
lists = [l.split()for l in ["ADMIRERS ASTIR BLACK DITHER DRINK HOAGIES JOLTS","OKRA PREMISE STRICKERS SURFACED SWARM WILTS WRAP","ARK CHILDREN'S CUIRASS FOR HOE ISOMER LANE","LORDS NOCTURNES RIDDLE SAT SOLE TRIONYM TROPE"]]

text = """R1 on the R6 
B2 B4 
R5 R11 of the B11 B12 
The B10 B5 B3 
B7 of the B13 B6 
... and the R3 B1 
R4 R9 
R13 R8 
R10 B14 
R2 R12 
B8 of the R14 
R7 of a B9 
"""

def scrabble(w):
    d={
        1:'AEILNORSTU',
        2:'DG',
        3:'BCMP',
        4:'FHVWY',
        5:'K',
        8:'JX',
        10:'QZ',
       }
    return sum(n*w.count(c) for n,s in d.items()for c in s)

def score(w):
    return sum(ord(c)%32 for c in w if c.isalpha())

def f(R,B):
    s=text[:]
    for i,w in enumerate(sorted(R),1):
        s = s.replace('R'+str(i)+' ',''+w+' ')
    for i,w in enumerate(sorted(B),1):
        s = s.replace('B'+str(i)+' ',''+w+' ')
    r=''
    for l in s.splitlines():
        v=sum(map(int,re.findall(r'-?\d+',l)))%26
        r+=chr(65+v)
    return r

lists = [[str(scrabble(w))for w in l]for l in lists]
a,b,c,d=lists


R=a+b
B=c+d
print(f(R,B))
print(f(B,R))

R=a+c
B=b+d
print(f(R,B))
print(f(B,R))

R=sum(zip(a,b),tuple())
B=sum(zip(c,d),tuple())
print(f(R,B))
print(f(B,R))

