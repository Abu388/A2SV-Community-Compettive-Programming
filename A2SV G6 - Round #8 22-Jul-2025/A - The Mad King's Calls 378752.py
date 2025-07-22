# Problem: A - The Mad King's Calls - https://codeforces.com/gym/599383/problem/A

from itertools import accumulate # to work on prefix
from collections import Counter, defaultdict,deque
from math import ceil
def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())

t=test()
for _ in range(t):
    nums=test()
    s=str(nums)

    cur = (int(s[0])-1)*10
    if len(s) == 1:
        print(cur+1)
    elif len(s) == 2:
        print(cur+3)
    elif len(s) == 3:
        print(cur+6)
    elif len(s) == 4:
        print(cur+10)
        