
_pow = pow
from math import *
pow = _pow
r=[]
r=r[0]
s=''
for c in r:s+=f'{int(c,16):04b}'

def get_packet(s):
    v=int(s[:3],2)
    s=s[3:]
    t=int(s[:3],2)
    s=s[3:]
    if t==4:
        n=''
        while 1:
            a=s[0]
            n+=s[1:5]
            s=s[5:]
            if a=='0':
                break
        P=(v,t,n,int(n,2))
    else:
        lt=s[0]
        s=s[1:]
        if lt=='0':
            l=int(s[:15],2)
            s=s[15:]
            P=(v,t,lt,l)
        else:
            l=int(s[:11],2)
            s=s[11:]
            P=(v,t,lt,l)
    return P,s
        
def get_packets(s,count=999):
    P=[]
    while len(s)>5 and count>0:
        count-=1
        p,s = get_packet(s)
        v,t,*x=p
        if t==4:
            P+=(p,[]),
        else:
            lt,l=x
            if lt=='0':
                S=s[:l]
                s=s[l:]
                P+=(p,get_packets(S)[0]),
            else:
                p1,s=get_packets(s,l)
                P+=(p,p1),
    return P,s

packs,s=get_packets(s)

def sum_version(P):
    v=0
    for p,s in P:
        w,*x=p
        v+=w
        v+=sum_version(s)
    return v

print(sum_version(packs))

def calc(P):
    p,s=P
    v,t,*x=p
    S=[*map(calc,s)]
    if t==0:
        return sum(S)
    elif t==1:
        return prod(S)
    elif t==2:
        return min(S)
    elif t==3:
        return max(S)
    elif t==4:
        return x[-1]
    elif t==5:
        a,b=S
        return int(a>b)
    elif t==6:
        a,b=S
        return int(a<b)
    elif t==7:
        a,b=S
        return int(a==b)
    
print(calc(packs[0]))






##############




def make_packet_tree(bits):
    packet = {
        "version": int(bits[0:3], 2),
        "type_id": int(bits[3:6], 2),
        "children": []
    }
    if packet["type_id"] == 4:
        packet["value"], bit_remainder = read_literal_value(bits[6:])
        return packet, bit_remainder
    return make_packet_with_sub_packets(bits, packet)


def read_literal_value(bits):
    bit_remainder = bits
    not_last = True
    binary_digits = ""
    while not_last:
        not_last = bit_remainder[0] != "0"
        digit_chunk = bit_remainder[1:5]
        bit_remainder = bit_remainder[5:]
        binary_digits = binary_digits + digit_chunk
    return int(binary_digits, 2), bit_remainder


def make_packet_with_sub_packets(bits, packet):
    length_type_id = bits[6]
    if length_type_id == "0":
        length_of_sub_packets = int(bits[7:22], 2)
        sub_remainder = bits[22:22 + length_of_sub_packets]
        bit_remainder = bits[22 + length_of_sub_packets:]
        while len(sub_remainder) > 0:
            sub_packet, sub_remainder = make_packet_tree(sub_remainder)
            packet["children"].append(sub_packet)
    else:
        number_of_sub_packets = int(bits[7:18], 2)
        bit_remainder = bits[18:]
        for _ in range(number_of_sub_packets):
            sub_packet, bit_remainder = make_packet_tree(bit_remainder)
            packet["children"].append(sub_packet)
    return packet, bit_remainder



############



import sys
from operator import mul

OPS = [ sum, lambda x:reduce(mul, x),
        min, max, None,
        lambda x:int(x[0] > x[1]),
        lambda x:int(x[0] < x[1]),
        lambda x:int(x[0] == x[1]) ]

class PacketStream():
    def __init__(self, data):
        self.data = bin(int('1'+data.strip(),16))[3:]
        self.pos = 0
        self.versions = 0

    def read(self, n):
        self.pos += n
        return int(self.data[self.pos-n:self.pos], 2)

    def readpacket(self):
        self.versions += self.read(3)
        tid = self.read(3)
        if tid == 4:
            v = 0
            while True:
                flag = self.read(1)
                v = (v << 4) + self.read(4)
                if flag == 0: return v
        vals = []
        if self.read(1) == 0:
            n = self.read(15)
            limit = self.pos + n
            while self.pos < limit:
                vals.append(self.readpacket())
        else:
            vals = [self.readpacket() for i in range(self.read(11))]
        return OPS[tid](vals)

if __name__ == '__main__':
    for line in open(sys.argv[1]).readlines():
        stream = PacketStream(line)
        result = stream.readpacket()
        print 'part 1:', stream.versions, 'part 2:', result
