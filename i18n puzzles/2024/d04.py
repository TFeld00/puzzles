DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
from datetime import *
import locale
import pytz

r=[]

with open(f'{DAY}.txt', 'r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        r+=[l]
        
        
r = parse_no_headers(r)

locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')
zero = datetime(1900,1,1,tzinfo=timezone.utc)

def parse(l):
    _,a,*ta=l
    ta=' '.join(ta)
    tz = pytz.timezone(a)
    d=datetime.strptime(ta,'%b %d, %Y, %H:%M')
    d=tz.localize(d)
    d=d.astimezone(timezone.utc)
    s=(d-zero).total_seconds()
    return int(s//60)
    
t=0
for a,b in r:
    t1=parse(a)
    t2=parse(b)
    t+=t2-t1

print(t)