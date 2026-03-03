DAY,_,_=__file__.rpartition('.')

import base64

t=''
with open(f'{DAY}_i.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        t+=l

FROM = (10<<24)+(1<<16)+(1<<8)+(10)
TO =   (10<<24)+(1<<16)+(1<<8)+(200)
WORD = 0xffff


def carry_around_add(a, b):
    c = a + b
    return (c & WORD) + (c >> 16)

def chk(data):
    s=0
    for i in range(0,len(data),16):
        s = carry_around_add(s,int(data[i:i+16],2))
    return ~s&WORD

def chk(data):
    if len(data)%16:
        data += '0'*8
    s=0
    for i in range(0,len(data),16):
        s += int(data[i:i+16],2)
    if s>WORD:
        s=s%(2**16) + (s>>16)
    return s^WORD

def udphead(ip,l):
    return ip[96:160] +\
        '0'*8 + format(17,'08b') + format(l+8,'016b')

with open(f'{DAY}_o.txt','wb')as F:
    b = base64.a85decode(t[2:-2])
#    
    
    while b:
        ip,b = b[:20],b[20:]
        udp,b = b[:8],b[8:]

        ip=''.join(format(byte, '08b') for byte in ip)
        udp=''.join(format(byte, '08b') for byte in udp)

        l=int(ip[16:32],2)-28
        payload,b = b[:l],b[l:]

        src=int(ip[96:128],2)
        dst=int(ip[128:160],2)
        dst_port = int(udp[16:32],2)

        chk_ip=chk(ip)
        chk_udp=chk(udphead(ip,l)+udp[:]+''.join(format(byte, '08b') for byte in payload))
        udp=udphead(ip,l)+udp


        if src!=FROM:
            continue
        if dst!=TO:
            continue
        if dst_port!=42069:
            continue
        if chk_ip!=0:
            continue
        if chk_udp!=0:
            continue

    
        F.write(payload)
    