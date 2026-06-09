from queue import *

# Pure Python, usable speed but over 10x greater runtime than Cython version
def fill(data, start_coords, fill_value, fillable = None):
    """
    Flood fill algorithm
    
    Parameters
    ----------
    data : (M, N) list of lists
        Image with flood to be filled. Modified inplace.
    start_coords : tuple
        Length-2 tuple of ints defining (row, col) start coordinates.
    fill_value : int
        Value the flooded area will take after the fill.
    fillable : function(current, next). Should return true if next cell can be filled, based on current.
        
    Returns
    -------
    (Size of area filled, coords of area), ``data`` is modified inplace.
    """
    if fillable is None:
        fillable = lambda current, next: current == next
    
    W=len(data[0])
    H=len(data)
    x,y=start_coords
    orig_value = data[y][x]
    
    q=Queue()
    s=set()
    q.put((x,y,orig_value))

    if fill_value == orig_value:
        raise ValueError(f"Area already {fill_value}")

    s=set()
    count = 0
    while not q.empty():
        x,y,c=q.get()
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            X,Y=x+dx,y+dy
            if (X,Y)in s:continue
        
            if 0<=X<W and 0<=Y<H:
                n=data[Y][X]
                if fillable(c,n):
                    s|={(X,Y)}
                    q.put((X,Y,n))
                    count += 1
                    data[Y][X]=fill_value

    return (count, s)


def global_fill_dist(data, start_value, moves = ((-1,0),(1,0),(0,-1),(0,1))):
    """
    Global bfs
    calculates shortest path from every cell to certain cell type.
    
    Parameters
    ----------
    data : (M, N) list of lists
        Image with flood to be filled. Modified inplace.
    start_color : tuple
        Length-2 tuple of ints defining (row, col) start coordinates.

    Returns
    -------
    (Size of area filled, coords of area), ``data`` is modified inplace.
    """
       
    W=len(data[0])
    H=len(data)
    q=Queue()
    s=set()
    for j,l in enumerate(data):
        for i,c in enumerate(l):
            if c==start_value:
                q.put((i,j,0))
                s|={(i,j)}

    while not q.empty():
        x,y,l=q.get()

        for dx,dy in moves:
            X,Y=x+dx,y+dy
            if (X,Y)in s:continue

            s|={(X,Y)}
            if 0<=X<W and 0<=Y<H:
                q.put((X,Y,l+1))
                data[Y][X]=l+1
    return data

def global_fill_dist_diags(data, start_value):
    return global_fill_dist(data,start_value,((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)))