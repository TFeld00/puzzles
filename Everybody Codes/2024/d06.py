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
from alg.grid import word_search, pattern_search
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

def solve(part):

    t={}
    with open(f'{DAY}{part}.txt','r')as F:
        for l in F:
            l=l.rstrip('\n')
            a,*c=re.split(':|,',l)
            t[a]=t.get(a,[])+c

    s={}
    seen=set()
    q=[('RR','R')]
    for r,p in q:
        if r in seen:continue
        for v in t.get(r,[]):
            n=p+v if part=='a' else p+v[0]
            if v=='@':
                l=len(n)
                s[l]=s.get(l,[])+[n]
            else:
                q+=[v,n],
        seen|={r}
    for v,l in s.items():
        if len(l)==1:
            print(*l)
            break

solve('a')
solve('b')
solve('c')