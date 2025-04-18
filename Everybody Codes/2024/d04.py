DAY,_,_=__file__.rpartition('.')

import os
from itertools import *
from collections import *
_pow = pow
from math import *
pow = _pow
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, whitespace, punctuation, printable
from alg.dijkstra import dijkstra
from img.img import read_img, write_img, write_img_fromlist     #write_img(DAY,COLS)
from alg.util import parse_with_headers, parse_skip_headers, parse_no_headers
from alg.util import get_neigbors_both, get_neigbors_diag, get_neigbors_orto, get_neighbor_positions, get_neighbor_positions_complex
from alg.util import get_bounds, get_bounds_complex, get_bounds_complex_dict
from alg.util import rotate90clockwise, rotate180, rotate90counterclockwise
from alg.floodfill import fill, global_fill_dist, global_fill_dist_diags
from alg.cellular import step_dict, step_list, to_dict, to_lists, step_function_game_of_life
from alg.string import shift_caesar, tr, block_print, readable_number, findall_overlapping
from alg.geom import area, area_pixels
from functools import *
from fractions import *
from textwrap import wrap
from datetime import *
from queue import *
import heapq #heapq.nsmallest
from functools import cache
import sympy    #sympy.primefactors, sympy.solve, sympy.sympify, etc..
import re
import sys
import z3
import networkx as nx

COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
}

r=[]
s=0
t=''

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]

print(sum(r)-min(r)*len(r))

# -----------------------

r=[]
s=0
t=''

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]

print(sum(r)-min(r)*len(r))

# -----------------------

r=[]
s=0
t=''

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]        

a=sorted(r)[len(r)//2]
print(a,sum(abs(v-a) for v in r))