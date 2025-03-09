DAY,_,_=__file__.rpartition('.')

from collections import *
from datetime import *

r=[]

format=f'%Y-%m-%dT%H:%M:%S%z'

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        
        l=datetime.strptime(l,format).astimezone(timezone.utc)#.replace(tzinfo=timezone.utc)

        r+=[l]
        
dt=Counter(r).most_common(1)[0][0]
print(dt.isoformat())

