DAY,_,_=__file__.rpartition('.')

import math

r=[]
with open(f'{DAY}.1.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=l,

w,h=len(r[0]),len(r)

print(w + h - math.gcd(w,h))

# ---

r=[]
with open(f'{DAY}.2.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=l,

w,h=len(r[0]),len(r)

def get_visited_squares(w: int, h: int) -> list[tuple[int, int]]:
    """
    Returns all 0-indexed grid squares visited by a straight line 
    from (0,0) to (W,H) using exact integer arithmetic.
    """
    x, y = 0, 0
    visited = [(x, y)]
    
    # Scale coordinates by W and H to avoid floating-point math.
    # Next vertical boundary is at x + 1. Scaled coordinate value is (x + 1) * H.
    # Next horizontal boundary is at y + 1. Scaled coordinate value is (y + 1) * W.
    while x < w - 1 or y < h - 1:
        next_vertical_crossing = (x + 1) * h
        next_horizontal_crossing = (y + 1) * w
        
        if next_vertical_crossing < next_horizontal_crossing:
            x += 1
        elif next_horizontal_crossing < next_vertical_crossing:
            y += 1
        else:
            # The line passes perfectly through a grid corner node.
            # It cleanly exits the current square into the diagonal neighbor.
            x += 1
            y += 1
            
        visited.append((x, y))
        
    return visited

PRICES={}

prices = {
    "Fresh Water": 199.80,
    "Charcoal": 259.30,
    "Grain": 299.20,
    "Mushrooms": 399.70,
    "Giant Fish": 459.90,
    "Berries": 599.10,
    "Glass": 649.40,
    "Honey": 699.00,
    "Amber": 749.70,
    "Quartz": 799.50,
    "Shells": 849.10,
    "Gems": 899.40,
    "Gold": 899.60,
}

materials = {
    "Mud": "Fresh Water",
    "Volcanic Ash": "Charcoal",
    "Grass": "Grain",
    "Fallen Logs": "Mushrooms",
    "Deep Water": "Giant Fish",
    "Thorns": "Berries",
    "Sand": "Glass",
    "Flowers": "Honey",
    "Forests": "Amber",
    "Permafrost": "Quartz",
    "Shallow Water": "Shells",
    "Pebbles": "Gems",
    "Rocks": "Gold",
}


s="""L and Y: Mud
Z and D: Volcanic Ash
G and V: Grass
O and T: Fallen Logs
N and U: Deep Water
A and K: Thorns
M and C: Sand
I and Q: Flowers
H and F: Forests
J and R: Permafrost
E and X: Shallow Water
S and W: Pebbles
P and B: Rocks""".split('\n')
for l in s:
    a,_,b,c=l.split(' ',3)
    PRICES[a]=prices[materials[c]]
    PRICES[b[0]]=prices[materials[c]]

s=0
for x,y in get_visited_squares(w,h):
    c=r[y][x]
    s+=PRICES[c]
print(math.ceil(s))