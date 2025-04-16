# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

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
    n , k = arr()
    if k >= n or k == n-1:
        print(1)
    else:
        print(n)