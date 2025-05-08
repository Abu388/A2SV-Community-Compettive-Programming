# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E


import bisect #arr = [1, 2, 4, 4, 5] , index = bisect.bisect_right(arr, 4)
import sys
from fractions import Fraction # to use fraction
import sys, threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
input = sys.stdin.readline
from heapq import *
from itertools import accumulate # to work on prefix
from collections import Counter, defaultdict,deque
from math import ceil,floor
def arr(): return list(map(str,  input().split()))#strip
def test(): return int(input())

n , m = arr()
n , m = int(n) , int(m)
parent = [i for i in range(n+1)]
size = [1] * (n + 1)

def find(x):
    stk  = []
    while parent[x] != x:
        stk.append(x)
        x = parent[x]        
    while stk:
        parent[stk.pop()] = x
    return parent[x]
def union(x,y):
    xu = find(x)
    yu = find(y)     
    if size[xu] > size[yu]:
        size[xu] += size[yu]
        parent[xu] = yu
    else:        
        size[yu] += size[xu]
        parent[yu] = xu

heap = []

for _ in range(m):
    a, b, w = arr()
    a , b , w = int(a) , int(b), int(w)
    a= a-1
    b=b-1
    heappush(heap,(w,a,b))
res = 0
while heap:
    w,a,b = heappop(heap)
    rep_a =find(a)
    rep_b = find(b)
    if rep_a != rep_b:
        res += w
        union(a,b)
print(res)