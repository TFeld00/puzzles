DAY,_,_=__file__.rpartition('.')

from alg.cellular import step_dict, step_list, to_dict, to_lists, step_function_game_of_life, get_neigbors_list

for part in 'abc':
    r=[]

    with open(f'{DAY}{part}.txt','r')as F:
        for l in F:
            l=l.rstrip('\n')
            l=list(l)
            r+=[l]            
            
    W,H=len(r[0]),len(r)

    M=r
    M[H//2][W//2] = '#'

    q=[[H//2,W//2]]
    for y,x in q:
        c=M[y][x]
        if c!='#' or (y,x)==(H//2,W//2):
            n=list(get_neigbors_list(M,y,x,'0'))
            if '#' in n and (n.count('1')+n.count('#')-(c=='1'))>=5:
                M[y][x]='#'
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        X, Y = x+dx, y+dy
                        if 0 <= X < W and 0 <= Y < H and M[Y][X]!='#':
                            q.append([Y,X])
                
    print(end='#')
    if part=='a':
        print('', sum(l.count('#')for l in M))
        continue

    for l in M:
        for i,c in enumerate(l):
            if c in '01':l[i]='.'

    #for l in M:print(''.join(l))

    def step_function_sand1(c,n):
        n=list(n)
        return '=' if c=='#' and '.' in n else c

    M=step_list(M,step_function_sand1, '.',False)

    #for l in M:print(''.join(l))

    def step_function_sand(c,n):
        n=list(n)
        return '=' if c!='=' and (n.count('='))>=5 else c

    while 1:
        x=[list(v)for v in M]
        M=step_list(M,step_function_sand, '0',False)
        if x==M:break
    #print(sum(l.count('=')for l in M))

    print(end='=')
    if part=='b':
        print('', sum(l.count('=')for l in M))
        continue


    def step_function_tree(c,n):
        n=list(n)
        return '@' if c=='#' and (n.count('#') + n.count('@'))==20 else c

    def get_neigbors_list_tree(m:list, y, x, default):
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                if abs(dx)==abs(dy)==2:continue
                if dx==dy==0:continue
                X, Y = x+dx, y+dy
                if 0 <= X < len(m[0]) and 0 <= Y < len(m):
                    yield m[Y][X]
                else:
                    yield default


    while 1:
        x=[list(v)for v in M]
        M=step_list(M,step_function_tree, '0',False, get_neigbors_function=get_neigbors_list_tree)
        if x==M:break


    #for l in M:print(''.join(l))

    def step_function_tree(c,n):
        n=list(n)
        return '@' if c=='#' and (n.count('@'))>=4 and n.count('=')==0 else c


    for _ in range(2):
        M=step_list(M,step_function_tree, '0',False)

    #for l in M:print(''.join(l))

    print('@', sum(l.count('@')for l in M))