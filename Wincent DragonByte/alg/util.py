def parse_with_headers(F, func = None):
    d = {}
    n = ''
    r = []
    for l in F:
        if not l:
            d[n] = r
            n = ''
            r = []
        elif l and not n:
            n = l
        elif n:
            if func:
                l=func(l)
            r += [l]
    if r:
        d[n] = r
    return d


def parse_no_headers(F, func = None):
    d = []
    r = []
    for l in F:
        if not l:
            d += [r]
            r = []
        else:
            if func:
                l=func(l)
            r += [l]
    if r:
        d += [r]
    return d


def parse_skip_headers(F, func = None):
    d = []
    r = []
    n = ''
    for l in F:
        if not l:
            d += [r]
            n = ''
            r = []
        elif l and not n:
            n = l
        elif n:
            if func:
                l=func(l)
            r += [l]
    if r:
        d += [r]
    return d


def get_neigbors_orto(m, y, x):
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        X, Y = x+dx, y+dy
        if 0 <= X < len(m[0]) and 0 <= Y < len(m):
            yield (Y, X, m[Y][X])


def get_neigbors_diag(m, y, x):
    for dx in (-1, 1):
        for dy in (-1, 1):
            X, Y = x+dx, y+dy
            if 0 <= X < len(m[0]) and 0 <= Y < len(m):
                yield (Y, X, m[Y][X])


def get_neigbors_both(m, y, x, includeSelf=False):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == dy == 0 == includeSelf:
                continue
            X, Y = x+dx, y+dy
            if 0 <= X < len(m[0]) and 0 <= Y < len(m):
                yield (Y, X, m[Y][X])

def get_neighbor_positions(y,x, includeSelf=False):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == dy == 0 == includeSelf:
                continue
            X, Y = x+dx, y+dy
            yield Y, X

def get_neighbor_positions_complex(p, includeSelf=False):
    for dx in (-1, 0, 1):
        for dy in (-1j, 0, 1j):
            if dx == dy == 0 == includeSelf:
                continue
            yield p+dx+dy

def get_bounds_complex(s:set):
    minX=min(int(v.real)for v in s)
    maxX=max(int(v.real)for v in s)
    minY=min(int(v.imag)for v in s)
    maxY=max(int(v.imag)for v in s)
    return minX,maxX,minY,maxY

def get_bounds_complex_dict(d:dict):
    return get_bounds_complex({*d.keys()})

def get_bounds(m:list,function):
    X,Y=set(),set()
    for y,l in enumerate(m):
        for x,c in enumerate(l):
            if function(c):
                X|={x}
                Y|={y}
    return min(X),max(X),min(Y),max(Y)

def rotate90clockwise(m:list):
    return [*zip(*m[::-1])]
def rotate90counterclockwise(m:list):
    return [*zip(*m)][::-1]
def rotate180(m:list):
    return [l[::-1] for l in m[::-1]]