DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}a.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]
        

s=0
for v in r:
    s+=v//10
    v%=10
    s+=v//5
    v%=5
    s+=v//3
    v%=3
    s+=v

print(s)

# -----------

r=[]
with open(f'{DAY}b.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]
        
coins=[1, 3, 5, 10, 15, 16, 20, 24, 25, 30]


def calc(coins, amount):
    dp = [0] + [amount+1] * amount
    for coin in coins:
        for x in range(coin, amount+1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != amount+1 else -1


s=0
for v in r:
    s+=calc(coins,v)

print(s)

# -----------

r=[]
with open(f'{DAY}c.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]
        
coins=[1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]

s=0
for v in r:
    s+=v//101 + (1 if v%202 else 0)
print(s)