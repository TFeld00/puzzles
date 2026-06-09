DAY,_,_=__file__.rpartition('.')

PI=[int(d) for d in '3141592653589793']

def shift(c,n):
    v=ord(c)%32-1
    v= (v-n)%26
    v += ord('A') if c.isupper() else ord('a')
    return chr(v)

r=''
with open(f'{DAY}_1.txt','r')as F:
    i=0
    for l in F:
        for c in l:
            if c.isalpha():
                r+=shift(c,PI[i])
            else:
                r+=c
            i=(i+1)%len(PI)

print(r)
s = ''.join(c for c in r if c.isalpha()).lower()

r=1
for n,v in [
        (0,'zero'),
        (1,'one'),
        (2,'two'),
        (3,'three'),
        (4,'four'),
        (5,'five'),
        (6,'six'),
        (7,'seven'),
        (8,'eight'),
        (9,'nine'),
        (10,'ten'),
    ]:
    r*=n**s.count(v)
print(r)