DAY,_,_=__file__.rpartition('.')

r=[]
with open(f'{DAY}.1.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=l.split(','),

r.pop(0)

r.sort(key=lambda x:[int(x[1]),x[2],int(x[3])])

print(''.join(s[0][0]for s in r))
# ---

r=[]
with open(f'{DAY}.2.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=l.split(','),

r.sort(key=lambda x:x[1])

g=[''.join(a)for a in zip(*[iter([c for x in r for c in x[0][:3]]+[c for x in r for c in x[0][3:]])]*6)]

D={
    '100000':'A',
    '110000':'B',
    '100100':'C',
    '100110':'D',
    '100010':'E',
    '110100':'F',
    '110110':'G',
    '110010':'H',
    '010100':'I',
    '010110':'J',
    '101000':'K',
    '111000':'L',
    '101100':'M',
    '101110':'N',
    '101010':'O',
    '111100':'P',
    '111110':'Q',
    '111010':'R',
    '011100':'S',
    '011110':'T',
    '101001':'U',
    '111001':'V',
    '010111':'W',
    '101101':'X',
    '101111':'Y',
    '101011':'Z',
    '000000':' ',
    
}


print(''.join(D[c]for c in g))