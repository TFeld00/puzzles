DAY,_,_=__file__.rpartition('.')

s=0

def valid(s):
    if len(s)<4:return False
    if len(s)>12:return False
    if not any(c.isdigit()for c in s):return False
    if not any(c.isupper()for c in s):return False
    if not any(c.islower()for c in s):return False
    if not any(ord(c)>127 for c in s):return False
    return True
    

with open(f'{DAY}.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')

        if valid(l):s+=1

print(s)
