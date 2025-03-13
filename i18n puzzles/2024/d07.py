DAY,_,_=__file__.rpartition('.')

from datetime import *
import pytz

r=[]

with open(f'{DAY}.txt', 'r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split('\t')
        r+=[l]

s=0
i=0

for t,a,b in r:
    d=datetime.fromisoformat(t)
    tzh = pytz.timezone('America/Halifax')
    tzs = pytz.timezone('America/Santiago')
    d2=datetime.fromisoformat(t).astimezone(tzh)
    
    T=tzh
    if d2.utcoffset()==d.utcoffset():
        T=tzh
    else:
        T=tzs
    
    d -= timedelta(minutes=int(b))
    d += timedelta(minutes=int(a))
    d = d.astimezone(T)

    i+=1
    s+=d.hour*i

print(s)