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


cubes = []
for i in range(0,len(cards),5):
    cubes+=cards[i:i+5],

def all_lines(part):
    if part == 1:
        bingo_lines = generate_hypercube_bingo_lines(5,2)
        return [set([cubes[i][j][k][l]for (k,l) in v])for i in range(5) for j in range(5) for v in bingo_lines]
    elif part == 2:
        bingo_lines = generate_hypercube_bingo_lines(5,3)
        return [set([cubes[i][j][k][l]for (j,k,l) in v])for i in range(5) for v in bingo_lines]
    else:
        bingo_lines = generate_hypercube_bingo_lines(5,4)
        return [set([cubes[i][j][k][l]for (i,j,k,l) in v])for v in bingo_lines]

def run(part):
    called=set()
    lines = all_lines(part)
    for n in nums:
        called.add(n)
        if sum(l <= called for l in lines)>4:print(n);break

run(1)
run(2)
run(3)