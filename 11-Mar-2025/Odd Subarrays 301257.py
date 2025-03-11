# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

from collections import Counter, defaultdict,deque
from math import ceil
def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())
t=test()
for _ in range(t):
    n=test()
    nums=arr()
    count=0
    stk=[]
    for i in nums:
        if stk and i <stk[-1]:
            stk=[]
            count+=1
        else:
            stk.append(i)

    print(count)