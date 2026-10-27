DAY,_,_=__file__.rpartition('.')

from functools import *

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        x=[]
        for a,b,c in l:
            if b=='>':a,c=c,a
            x+=[a,c],
        r+=[x]
        
s=0
for l in r:
    i={v for x in l for v in x}
    
    w=''.join(sorted(i,key=cmp_to_key(lambda a,b:1 if [a,b] in l else -1)))
    s+=int(w)
print(s)

# ---


r=[]

with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        x=[]
        for a,b,c in l:
            if b=='>':a,c=c,a
            x+=[a,c],
        r+=[x]
        
s=0
for l in r:
    i={v for x in l for v in x} 
    d={}
    for a,b in l:
        d[a]=d.get(a,[])+[b]
    for a in sorted(i):
        if sum(a in v for v in l)<len(i)-1:
            c={v for w in d.get(a,[]) for v in d.get(w,[])}-{*d.get(a,[])}
            if c:
                l+=[a,c.pop()],
                break
    w=''.join(sorted(i,key=cmp_to_key(lambda a,b:1 if [a,b] in l else -1)))

    s+=int(w)
print(s)


# ---

r=[]

with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        x=[]
        for a,b,c in l:
            if b=='>':a,c=c,a
            x+=[a,c],
        r+=[x]
        
s=0
for l in r:
    i={v for x in l for v in x} 
    d={}
    for a in i:
        d[a]=set()
    for a,b in l:
        d[a]|={b}
    v=set()
    x=1
    while x:
        y=0
        for a in i:
            for b in i:
                if b in d[a]:
                    if d[b]-d[a]:y=1
                    d[a]|=d[b]
        x=y
    
    w=''.join(sorted(i,key=cmp_to_key(lambda a,b:1 if b in d.get(a,set()) else -1)))

    s+=int(w)
print(s)



# --- simpler versions with "proper" tpop-sort ---



def topological_sort_dfs(vertices, edges):
    # 1. Build adjacency list
    adj_list = {i: [] for i in vertices}
    for u, v in edges:
        adj_list[u].append(v)
        
    state = {i: 0 for i in vertices}
    stack = []
    
    def dfs(node):
        state[node] = 1 # Mark as Visiting
        
        for neighbor in adj_list[node]:
            if state[neighbor] == 0:
                dfs(neighbor)
                    
        state[node] = 2 # Mark as Visited
        stack.append(node) # Post-order addition
        return True

    # 3. Run DFS for every unvisited node
    for i in vertices:
        if state[i] == 0:
            dfs(i)
                
    return stack

print()
for part in 'abc':
    r=[]
    with open(f'{DAY}{part}.txt','r')as F:
        for l in F:
            l=l.rstrip('\n')
            l=l.split()
            x=[]
            for a,b,c in l:
                if b=='>':a,c=c,a
                x+=[a,c],
            r+=[x]
    s=0
    for l in r:
        i={v for x in l for v in x} 
        w=''.join(topological_sort_dfs(i,l))
        s+=int(w)
    print(s)
