# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

from collections import Counter, defaultdict
from math import ceil
def arr(): return list(map(int, (x for x in input().split())))
def test(): return int(input())
n=test()
nums=arr()
prefix=[0]
pre=[0]
total=0
for i in range(len(nums)):
    total+=nums[i]
    prefix.append(total)
nums.sort()
total=0
for i in range(len(nums)):
    total+=nums[i]
    pre.append(total)
m=test()
for _ in range(m):
    type,l,r=arr()
    if type==1:
        print(prefix[r]-prefix[l-1])
    else:
        print(pre[r]-pre[l-1])
