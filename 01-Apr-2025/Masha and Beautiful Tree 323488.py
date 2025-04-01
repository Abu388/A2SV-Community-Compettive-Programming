# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

from itertools import accumulate # to work on prefix
from collections import Counter, defaultdict,deque
from math import ceil,floor
def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())
 
global count 
 
 
def final(left,right):
    global count
    val = []
    if left[0] > right[0]:
        count += 1
        val = right + left
    else:
        val = left + right
    return val
 
n = test()
for _ in range(n):
    t =test()
    nums = arr()
    count = 0
 
    def merge(nums):
        if len(nums) == 1:
            return nums
        m = len(nums)//2
        left  =  merge(nums[:m])
        right =  merge(nums[m:])
        return final(left,right)
    res = merge(nums)
    if res == sorted(nums):
        print(count)
    else:
        print(-1)