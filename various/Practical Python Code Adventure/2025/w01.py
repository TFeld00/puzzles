DAY,_,_=__file__.rpartition('.')
import re

MORSE = """A	._	K	_._	U	.._
B	_...	L	._..	V	..._
C	_._.	M	__	W	.__
D	_..	N	_.	X	_.._
E	.	O	___	Y	_.__
F	.._.	P	.__.	Z	__..
G	__.	Q	__._	.	._._._
H	....	R	._.	?	..__..
I	..	S	...	!	_._.__
J	.___	T	_	-	_...._""".split()

D={}

for a,b in zip(*[iter(MORSE)]*2):
    D[b]=a

s=''
with open(f'{DAY}.1.txt','r', encoding='utf8')as F:
    for l in F:
        for w in l.split():
            s+=D[w]
        s+=' '
print(s)
print()

# ---

s=''
with open(f'{DAY}.2.txt','r', encoding='utf8')as F:
    for l in F:
        for c in l:
            s+=str(ord(c))

print(s)
b=bin(int(s))[2:].translate(str.maketrans('01','._'))
l=b.split('_._.__')[3:-3]

s=''
for c in l:
    s+=D[c]
print(s)