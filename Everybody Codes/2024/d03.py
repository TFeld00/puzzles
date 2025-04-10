DAY,_,_=__file__.rpartition('.')
PATH,YEAR,_ = DAY.rsplit('\\',2)

import enum
import sys
sys.path.append(PATH)
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
import heapq
from functools import cache
import sympy    #sympy.primefactors, sympy.solve, sympy.sympify, etc..
import re
import z3
import networkx as nx

COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
}

#from alg.file import download_input
#download_input(DAY,YEAR)

cols = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
}
for i in range(11):
    cols['%X'%(i)] = (255-25*i,255-25*i,255-25*i)
    cols[i] = (255-25*i,255-25*i,255-25*i)

def solve(part):
    r=[]
    with open(f'{DAY}{"abc"[part-1]}.txt','r')as F:
        for l in F:
            l=l.rstrip('\n')
            r+=[list('.'+l+'.')]
            
    W,H=len(r[0]),len(r)+2

    r=[list('.'*(W))]+r
    r+=list('.'*(W)),

    if part < 3:
        global_fill_dist(r,'.')
    else:
        global_fill_dist_diags(r,'.')

    print(sum(sum(v for v in l if type(v)==int)for l in r))
    write_img_fromlist(r,f'{DAY}{"abc"[part-1]}',cols)


solve(1)
solve(2)
solve(3)