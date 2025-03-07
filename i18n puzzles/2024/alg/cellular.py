def to_dict(m:list, map_function=lambda v: v):
    d = {}
    for i, l in enumerate(m):
        for j, v in enumerate(l):
            d[(i, j)] = map_function(v)
    return d


def get_neigbors_dict(d:dict, y, x, default):
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            X, Y = x+dx, y+dy
            yield d.get((Y, X), default)


def get_neigbors_list(m:list, y, x, default):
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            X, Y = x+dx, y+dy
            if 0 <= X < len(m[0]) and 0 <= Y < len(m):
                yield m[Y][X]
            else:
                yield default


def step_dict(d:dict, step_function, default, expandable=True):
    D = {}
    b,a = zip(*d.keys())
    x, X, y, Y = min(a), max(a)+1, min(b), max(b)+1
    if (not expandable) or all(d.get((i,x),default)==default for i in range(y, Y)):x+=1
    if (not expandable) or all(d.get((i,X-1),default)==default for i in range(y, Y)):X-=1
    if (not expandable) or all(d.get((y,j),default)==default for j in range(x, X)):y+=1
    if (not expandable) or all(d.get((Y-1,j),default)==default for j in range(x, X)):Y-=1
    
    for i in range(y-1, Y+1):
        for j in range(x-1, X+1):
            D[(i, j)] = step_function(d.get(i,{}).get(j,default), get_neigbors_dict(d, i, j, default))
    return D


def step_list(m:list, step_function, default, expandable=True):
    M = []
    x, X, y, Y = 0, len(m[0]), 0, len(m)
    if (not expandable) or all(m[i][x]==default for i in range(y, Y)):x+=1
    if (not expandable) or all(m[i][X-1]==default for i in range(y, Y)):X-=1
    if (not expandable) or all(v==default for v in m[y]):y+=1
    if (not expandable) or all(v==default for v in m[Y-1]):Y-=1
    
    for i in range(y-1, Y+1):
        L = []
        for j in range(x-1, X+1):
            L += step_function(m[i][j], get_neigbors_list(m, i, j, default)),
        M += L,
    return M


def to_lists(d:dict, map_function=lambda v: v, default=0):
    x, y = zip(*d.keys())
    m = [[
        map_function(d.get((i, j), default))
        for j in range(min(x), max(x)+1)]
        for i in range(min(y), max(y)+1)]
    return m


def step_function_game_of_life(alive2alive:list, dead2alive:list):
    return lambda c,n:(sum(n)-1 in alive2alive) if c else (sum(n)in dead2alive)
    
def parse_list(m:list, on:str):
    return [[c==on for c in l]for l in m]


"""
m=parse_list(r,'#')
for _ in range(100):
    m=step_list(m, step_function_game_of_life([2,3],[3]), False, False)
    #m[0][0]=True
print(sum(map(sum,m)))

---

m=to_dict(r,lambda v:v=='#')
for _ in range(100):
    m=step_dict(m, step_function_game_of_life([2,3],[3]), False)    
    #m[(0,0)]=True
print(sum(m.values()))
"""