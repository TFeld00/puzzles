DAY,_,_=__file__.rpartition('.')

from datetime import *
import pytz

r=[]

with open(f'{DAY}.txt', 'r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split('; ')
        r+=[l]
        
def parse(a,b):
    tz = pytz.timezone(b)

    d=datetime.strptime(a,'%Y-%m-%d %H:%M:%S')
    d=tz.localize(d)

    d=d.astimezone(timezone.utc)
    x=[]
    offsets=[0]
    if b=='Africa/Casablanca':
        offsets +=-4,
    if b=='Africa/Juba':
        offsets +=-4,
    if b=='Africa/Sao_Tome':
        offsets +=-4,
    if b=='America/Mazatlan':
        offsets +=4,
    if b=='America/Mexico_City':
        offsets +=-4,
    if b=='America/Santiago':
        offsets +=-4,-4
    if b=='Antarctica/Casey':
        offsets +=12,
    if b=='Antarctica/Vostok':
        offsets +=-8,
    if b=='Asia/Hebron':
        offsets +=-4,4,
    if b=='Asia/Pyongyang':
        offsets +=2,
    if b=='Asia/Qyzylorda':
        offsets +=-4,4,
    if b=='Asia/Tehran':
        offsets +=-4,
    if b=='Europe/Volgograd':
        offsets +=-4,4,
    if b=='Pacific/Easter':
        offsets +=-4,4,
        
    for i in offsets:
        x+=d+timedelta(minutes=15*i),
    
    return {v.isoformat() for v in x}


D={}

for a,b in r:
    d=parse(a,b)
    D[b]=D.get(b,set())|{*d}


#print(*sorted(D),sep='\n')
print(*set.intersection(*D.values()))