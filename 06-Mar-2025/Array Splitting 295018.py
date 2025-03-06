# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

from collections import Counter, defaultdict
from math import ceil
def arr(): return list(map(int, (x for x in input().split())))
def test(): return int(input())

n,k=arr()
nums=arr()
k=k-1#what will happen if n will be 1?
prefix=[0]*n
for i in range(1,n):
    prefix[i]=nums[i]-nums[i-1]
prefix.sort()

total=0


for ind,i in enumerate(prefix):
    total+=i
    prefix[ind]=total


while k>0:
    prefix.pop()
    k-=1


print(prefix[-1])

