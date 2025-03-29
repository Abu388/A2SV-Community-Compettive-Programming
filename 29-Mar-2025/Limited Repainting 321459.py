# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

from itertools import accumulate # to work on prefix
from collections import Counter, defaultdict,deque
from math import ceil
def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())
t = test()
for _ in range(t):
    n , k = arr()
    s = input()
    val = arr()
    l,r = 0, max(val)
    def valid(mid):
        flag = False
        count = 0
        for i in range(len(s)):
            if not flag:
                if s[i] == 'B' and val[i] > mid:
                    flag = True
                    count += 1
            else:
                if s[i] == 'R' and val[i] > mid:
                    flag = False
        if count <= k:
            return True
        return False
    
    while l<=r:
        m = (l+r)//2
        if valid(m):
            r = m-1
        else:
            l = m+1
    print(l)