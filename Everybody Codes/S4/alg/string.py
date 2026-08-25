import re
from string import ascii_lowercase, ascii_uppercase

def shift_caesar(s,n):
    a=ascii_lowercase + ascii_uppercase
    b=ascii_lowercase[n%26:]+ascii_lowercase[n%26:] + ascii_uppercase[n%26:]+ascii_uppercase[n%26:]
    t=str.maketrans(a,b)
    
    return s.translate(t)

def tr(s,a,b):
    t=str.maketrans(a,b)
    return s.translate(t)

BLOCK_PRINT=' █'

def block_print(s:list):
    for l in s:
        print(''.join(BLOCK_PRINT[v]for v in l))

READABLE_DICT={
    0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
    11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
    20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',
    100:'hundred',
}
def readable_number(n):
    if type(n) != int: raise ValueError('Must be integer')
    if n>100:raise ValueError('TOO LARGE. Modify readable_number in string.py')

    if n not in READABLE_DICT:
        a,b=n//10,n%10
        if a:
            s=READABLE_DICT[a*10]
            if b:
                s+= ' ' +READABLE_DICT[b]
            READABLE_DICT[n] = s
    return READABLE_DICT[n]

def findall_overlapping(s,l):
    if type(l)==list:
        l='|'.join(l)
    return re.findall(rf'(?=({l}))', s)