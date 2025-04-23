# Problem: Belted Rooms - https://codeforces.com/problemset/problem/1428/B

import bisect #arr = [1, 2, 4, 4, 5] , index = bisect.bisect_right(arr, 4)
import sys
from fractions import Fraction # to use fraction
import sys, threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
input = sys.stdin.readline
from itertools import accumulate # to work on prefix
from collections import Counter, defaultdict,deque
from math import ceil,floor
def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())

t = test()
for _ in range(t):
    n = test()
    s = list(input().strip())
    
    if '<' in s and '>' in s:
        count = 0
        for i in range(n):
            if s[i] == '-' or s[(i+1)%n] == '-':
                count += 1
        print(count)
    else:
        print(n)




