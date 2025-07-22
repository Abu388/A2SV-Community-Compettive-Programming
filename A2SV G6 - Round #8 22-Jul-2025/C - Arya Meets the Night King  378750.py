# Problem: C - Arya Meets the Night King  - https://codeforces.com/gym/599383/problem/C

from collections import Counter, defaultdict,deque
from math import ceil,floor
def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())

s , b = arr()
nums = arr()
res = [0]*len(nums)
mp = defaultdict(int)
for l, i in enumerate(nums):
    mp[l] += i
smp = dict(sorted(mp.items(), key=lambda x:x[1]))

val = []
for _ in range(b):
    a , b = arr()
    val.append([a,b])

val.sort()
prifix = 0
for i in range(len(val)):
    prifix += val[i][1]
    val[i][1] = prifix

l = 0
for k , v in smp.items():
    
    if v < val[0][0]:
        res[k] = 0
    elif v >= val[len(val)-1][0]:
        
        res[k] = val[len(val)-1][1]
    else:
        
        while val[l][0] < v:
            l += 1
        if val[l][0] > v:
            l -= 1
        res[k] = val[l][1]
print(*res)



