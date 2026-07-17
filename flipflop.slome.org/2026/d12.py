DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}.txt', 'r') as F:
    i=-1
    for l in F:
        r+=[*map(int,l.split())],

nums,cards=[],[]
A=0
for v in r:
    if not v:
        A=1
    elif A:
        cards+=[v[i:i+5]for i in range(0,25,5)],
    else:
        nums+=v

def lines(card):
    rows=[*card]
    cols=[*zip(*card)]
    diags=[[card[i][i]for i in range(5)],[card[i][4-i]for i in range(5)]]
    lines = rows+cols+diags
    return map(set,lines)

called=set()
all_lines = []
for c in cards:all_lines+=lines(c)
for n in nums:
    called.add(n)
    if sum(l <= called for l in all_lines)>4:print(n);break

# ---

cubes = []
for i in range(0,len(cards),5):
    cubes+=cards[i:i+5],

def cube_lines(cube):
    res=set()
    for c in cube:
        res |= {*map(tuple,lines(c))}
    for c in zip(*cube):
        res |= {*map(tuple,lines(c))}
    for j in range(5):
        c=[]
        for k in range(5):
            c+=[cube[i][j][k]for i in range(5)],
        res |= {*map(tuple,lines(c))}
    res.add(tuple(cube[i][i][i]for i in range(5)))
    res.add(tuple(cube[i][4-i][i]for i in range(5)))
    res.add(tuple(cube[i][i][4-i]for i in range(5)))
    res.add(tuple(cube[i][4-i][4-i]for i in range(5)))
    res.add(tuple(cube[4-i][i][i]for i in range(5)))
    res.add(tuple(cube[4-i][4-i][i]for i in range(5)))
    res.add(tuple(cube[4-i][i][4-i]for i in range(5)))
    res.add(tuple(cube[4-i][4-i][4-i]for i in range(5)))
    
    return map(set,res)

all_lines2 = []
for c in cubes:
    all_lines2 += cube_lines(c)

called=set()
for n in nums:
    called.add(n)
    if sum(l <= called for l in all_lines2)>4:print(n);break

import itertools
def generate_hypercube_bingo_lines(size=5, dimensions=4):
    """
    Generates all unique horizontal, vertical, diagonal, and omni-directional
    winning lines for a 5x5x5x5 hypercube.
    """
    lines = []
    
    # 1. Generate all possible component movement directions (-1, 0, 1)
    # 0 = stationary coordinate, 1 = ascending index, -1 = descending index
    raw_directions = list(itertools.product([-1, 0, 1], repeat=dimensions))
    raw_directions.remove((0,) * dimensions)  # Remove the stationary point
    
    # 2. Filter out reverse duplicates (keep only lines starting with an ascending '1')
    unique_directions = []
    for d in raw_directions:
        for component in d:
            if component != 0:
                if component == 1:
                    unique_directions.append(d)
                break

    # 3. Calculate bounded anchor positions for each valid direction vector
    for d in unique_directions:
        coord_ranges = []
        for component in d:
            if component == 0:
                coord_ranges.append(list(range(size)))     # Any index is valid if stationary
            elif component == 1:
                coord_ranges.append([0])                   # Ascending must start at 0
            elif component == -1:
                coord_ranges.append([size - 1])            # Descending must start at max index
                
        # 4. Extrapolate coordinates across the 5 steps of the line
        for start_point in itertools.product(*coord_ranges):
            single_line = []
            for step in range(size):
                point = tuple(start_point[i] + (step * d[i]) for i in range(dimensions))
                single_line.append(point)
            lines.append(single_line)
            
    return lines

# Execute and profile the generation
bingo_lines = generate_hypercube_bingo_lines()
print()
all_lines3 = [set([cubes[i][j][k][l]for (i,j,k,l) in v])for v in bingo_lines]

called=set()
for n in nums:
    called.add(n)
    if sum(l <= called for l in all_lines3)>4:print(n);break