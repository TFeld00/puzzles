DAY,_,_=__file__.rpartition('.')

from collections import Counter
from PIL import Image


s=''
with open(f'{DAY}.1.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=l

C=Counter(s[i:i+4]for i in range(0,len(s),4))
D={v:x for x,v in C.items()}

print(D[1081],D[1055],D[965],sep='')

# ---

r=[]
with Image.open(f"{DAY}.2.png") as img:
    pixels = img.load()
    w, h = img.size
    for i in range(h):
        l = []
        for j in range(w):
            l += pixels[j, i],
        r += l

C=Counter(r)
x=[]
t=str.maketrans('0123456789','OIZEASGTBP')
for v,_ in C.most_common(3):
    s='%02X%02X%02X'%v
    x+=s.translate(t),
print(*x)