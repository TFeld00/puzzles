DAY,_,_=__file__.rpartition('.')

from PIL import Image

r=[]
with Image.open(f"{DAY}.1.png") as img:
    pixels = img.load()
    w, h = img.size
    for i in range(h):
        l = []
        for j in range(w):
            l += pixels[j, i],
        r += [l]

r=[v for l in r for v in l]
l=len(r)
x=int(l**0.5)

img = Image.new('RGB', (x,x), "white")
pixels = img.load()

d=1
for v in range(0,l,x):
    m=r[v:v+x][::d]
    d=-d
    for j, p in enumerate(m):
        pixels[j,v//x] = p

img.save(f"{DAY}.1.o.png")

# ---

img = Image.new('RGB', (x,x), "white")
pixels = img.load()

d=1
for i in range(1,x):
    m=r[:i][::d]
    d=-d
    r=r[i:]
    for j in range(i):
        pixels[j,i-j]=m[j]
for i in range(x,0,-1):
    m=r[:i][::d]
    d=-d
    r=r[i:]
    for j in range(i):
        pixels[x-i+j,x-j-1]=m[j]

img.save(f"{DAY}.2.o.png")
