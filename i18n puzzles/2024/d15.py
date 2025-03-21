DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
from datetime import *
import pytz

r = []

with open(f'{DAY}.txt', 'r', encoding='utf8') as F:
    for l in F:
        l=l.rstrip('\n')
        if l:l=l.split('\t')
        r+=[l]

A,B=parse_no_headers(r)

res = {}
a = datetime(2022, 1, 1, tzinfo=timezone.utc)
while a.year == 2022:
    res[a] = 0
    a += timedelta(minutes=15)

for x in A:
    tzh = pytz.timezone(x[1])
    h = x[2].split(';')
    h = [datetime.strptime(v, '%d %B %Y').date() for v in h]
    for v in res:
        w = v.astimezone(tzh)
        if w.date() in h:continue
        if w.weekday() > 4:continue
        if [w.hour, w.minute] < [8, 30]:continue
        if w.hour >= 17:continue

        res[v] = 1

D = []
for x in B:
    tzh = pytz.timezone(x[1])
    h = x[2].split(';')
    h = [datetime.strptime(v, '%d %B %Y').date() for v in h]
    o = 0
    for v in res:
        w = v.astimezone(tzh)
        if w.date() in h:continue
        if w.weekday() > 4:continue
        o += 1 - res[v]

    D += [o * 15]

print(max(D) - min(D))
