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

d={}
n=[]
s=0
t=''

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        #l=[*map(int,re.findall(r'-?\d+',l))]
        #l=[*map(int,l.split())]
        #l=[*map(int,l)]
        a,*l=[v.split('=')[1]for v in l.split(', ')]
        #l=int(l)
        #l=list(l)
        #print(l)
        d[int(a)]=l
        n+=[[a,*l]]
        #t+=l
        
        
    

R=[1,[],[]]
def order(R):
    if not R:return[]
    i,l,r=R
    if i==0:return[]
    return order(l)+[i]+order(r)

def insert(v,p,R):
    i,l,r=R
    if not i:return
    _,x,y,_ = d[i]
    if not l:
        if  x==p:
            R[1]=[v,[],[]]
            return 1
    elif insert(v,p,R[1]):
        return 1
    if not r:
        if y==p:
            R[2]=[v,[],[]]
            return 1
    elif insert(v,p,R[2]):
        return 1
    

for v,p,l,r,data in n[1:]:
    insert(int(v),p,R)
o=(order(R))
print(sum(i*v for i,v in enumerate(o,1)))


d={}
n=[]
s=0
t=''



with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        #l=[*map(int,re.findall(r'-?\d+',l))]
        #l=[*map(int,l.split())]
        #l=[*map(int,l)]
        a,*l=[v.split('=')[1].split()for v in l.split(', ')]
        #l=int(l)
        #l=list(l)
        #print(l)
        a=a[0]
        l=[set(v)for v in l]
        d[int(a)]=l
        n+=[[a,*l]]
        #t+=l
        
        
    

R=[1,[],[]]
def order(R):
    if not R:return[]
    i,l,r=R
    if i==0:return[]
    return order(l)+[i]+order(r)

def insert(v,p,R):
    i,l,r=R
    if not i:return
    _,x,y,_ = d[i]
    if not l:
        if x & p:
            R[1]=[v,[],[]]
            return 1
    elif insert(v,p,R[1]):
        return 1
    if not r:
        if y & p:
            R[2]=[v,[],[]]
            return 1
    elif insert(v,p,R[2]):
        return 1
    

for v,p,l,r,data in n[1:]:
    insert(int(v),p,R)
o=(order(R))
print(sum(i*v for i,v in enumerate(o,1)))




d={}
n=[]
s=0
t=''



with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        #l=[*map(int,re.findall(r'-?\d+',l))]
        #l=[*map(int,l.split())]
        #l=[*map(int,l)]
        a,*l=[v.split('=')[1].split()for v in l.split(', ')]
        #l=int(l)
        #l=list(l)
        #print(l)
        a=a[0]
        l=[set(v)for v in l]
        d[int(a)]=l
        n+=[[a,*l]]
        #t+=l
        
        
    

R=[1,[],[]]
def order(R):
    if not R:return[]
    i,l,r=R
    if i==0:return[]
    return order(l)+[i]+order(r)

def order2(R):
    if not R:return[]
    i,l,r=R
    if i==0:return[]
    return [[i,1]]+order2(l)+[[i,2]]+order2(r)

D={}
def insert(v,p,n):
    o=order2(R)
    o*=2
    if n in o:o=o[o.index(n)+1:]
    for i,s in o:
        l=D[i][s]
        x = d[i][s]
        if not l:
            if x & p:
                D[i][s]=D[v]
                return 1
        elif d[l[0]][0]!=x and x==p:
            D[i][s]=D[v]
            w,p=l[0],d[l[0]][0]
            return insert(w,p,order2(D[v])[-1])
    

D[1]=[1,[],[]]
R=D[1]
for v,p,l,r,data in n[1:]:
    D[int(v)]=[int(v),[],[]]
    insert(int(v),p,0)

o=(order(R))
print(sum(i*v for i,v in enumerate(o,1)))