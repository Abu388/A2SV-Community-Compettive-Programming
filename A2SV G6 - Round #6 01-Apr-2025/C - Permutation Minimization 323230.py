# Problem: C - Permutation Minimization - https://codeforces.com/gym/594077/problem/C

from collections import Counter, defaultdict, deque

from math import ceil
def arr(): return list(map(int, (x for x in input().split())))
def test(): return int(input())
t=test()
for _ in range(t):
    
    n=test()
    nums=arr()
    stk=deque()
    for i in nums:
        if  stk and stk[0]>i:
            stk.appendleft(i)
        else:
            stk.append(i)
    print(*stk)