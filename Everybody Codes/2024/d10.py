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


def runes(r,I=2,J=2):
    cols = [set(l[I-2:I+6])-{'.'}for l in zip(*r)]
    rows = [set(l[J-2:J+6])-{'.'}for l in r]
    undo = {}
    for i in range(I,I+4):
        l=r[i]
        for j in range(J,J+4):
            c=l[j]
            undo[(i,j)]=c
            if c=='.':
                s=(cols[j]&rows[i])
                if s:
                    c2=s.pop()
                    r[i][j] = c2
                    cols[j]-={c2}
                    rows[i]-={c2}
    for i in range(I,I+4):
        l=r[i]
        for j in range(J,J+4):
            c=l[j]
            if c=='.':
                if len(rows[i])==1 and '?'in cols[j]:
                    c2 =rows[i].pop()
                    for di in range(I-2,I+6):
                        if r[di][j]=='?':
                            undo[(di,j)]='?'
                            r[di][j]=c2
                    r[i][j] = c2
                elif len(cols[j])==1 and '?'in rows[i]:
                    c2 =cols[j].pop()
                    for dj in range(J-2,J+6):
                        if r[i][dj]=='?':
                            undo[(i,dj)]='?'
                            r[i][dj]=c2
                    r[i][j] = c2
    
    s=''
    for i in range(I,I+4):
        l=r[i]
        for j in range(J,J+4):
            s+=l[j]
    if '.' in s:
        for (i,j),c in undo.items():
            r[i][j]=c
    return s

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=list(l)
        r+=[l]

print(runes(r))


r=[]
s=0

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l.split()]

for x in parse_no_headers(r):
    for v in zip(*x):
        v=[list(l)for l in v]
        res = runes(v)
        s+= sum(i*(ord(c)-64) for i,c in enumerate(res,1))
print(s)


r=[]
s=0

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=list(l)
        r+=[l]

R=[]
for i in range(0,len(r)-2,6):
    rows = r[i:i+8]
    for j in range(0,len(r[0])-2,6):
        R+=(i,j),

D={}
for _ in range(2):
    for i,j in R:
        res = runes(r,i+2,j+2)
        D[(i,j)]=res
        
for res in D.values():
    if '.' in res:continue
    s+= sum(i*(ord(c)-64) for i,c in enumerate(res,1))
print(s)