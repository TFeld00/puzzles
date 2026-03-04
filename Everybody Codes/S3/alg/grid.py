from alg.util import rotate90clockwise, rotate180, rotate90counterclockwise

def word_search(m: list, word:list|str, includeDiagonals:bool = False):
    count = 0
    if type(word)==str:
        word = list(word)
    L=len(word)
    grid = [list(l)for l in m]

    for r in [grid, rotate90clockwise(grid), rotate180(grid), rotate90counterclockwise(grid)]:
        W,H=len(r[0]),len(r)
        for i,row in enumerate(r):
            for j in range(W-L+1):
                count += row[j:j+L]==word
                if includeDiagonals and i<=H-L:
                    count += all(r[i+k][j+k]==c for k,c in enumerate(word))

    return count

def pattern_search(m:list, pattern: list|str, rotate:bool=False, ignoreChar='.'):
    count = 0
    grid = [list(l)for l in m]
    if type(pattern) == str: pattern = pattern.split('\n')
    pattern = [list(l)for l in pattern]
    pW,pH = len(pattern[0]),len(pattern)

    grids = [grid]
    if rotate:
        grids += rotate90clockwise(grid),rotate180(grid),rotate90counterclockwise(grid)

    for r in grids:
        W,H=len(r[0]),len(r)
        for i in range(H-pH+1):
            for j in range(W-pW+1):
                chunk = [l[j:j+pW]for l in r[i:i+pH]]
                count += all(
                    all(a==ignoreChar or a==b for a,b in zip(patternRow, chunkRow)) for patternRow,chunkRow in zip(pattern,chunk)
                )
    return count