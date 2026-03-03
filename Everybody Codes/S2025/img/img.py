from PIL import Image

COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
}

def write_img(day, cols = COLS):
    r = []
    with open(f'{day}.txt', 'r') as F:
        for l in F:
            r += [l.rstrip('\n')]

    # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
    img = Image.new('RGB', (len(r[0]), len(r)), "white")
    pixels = img.load()  # create the pixel map

    for i, l in enumerate(r):
        for j, c in enumerate(l):
            pixels[j, i] = cols.get(c, (ord(c), 0, 255))

    img.save(f"{day}.png")

def read_img(day, cols=COLS):
    cols2 = {p: c for c, p in cols.items()}
    r = []
    with Image.open(f"{day}.png") as img:
        pixels = img.load()
        w, h = img.size
        for i in range(h):
            l = ''
            for j in range(w):
                R, G, B = pixels[j, i]
                l += cols2.get((R, G, B), chr(R))
            r += [l]

    with open(f'{day}_2.txt', 'w') as F:
        F.write('\n'.join(r) + '\n')


def write_img_fromlist(list,name, cols = COLS):
    r=list[:]

    # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
    img = Image.new('RGB', (len(r[0]), len(r)), "white")
    pixels = img.load()  # create the pixel map

    for i, l in enumerate(r):
        for j, c in enumerate(l):
            try:
                pixels[j, i] = cols.get(c, (ord(c)if type(c)==str else c, 0, 255))
            except:
                print(f"error: '{c}'")

    img.save(f"{name}.png")