# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

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
def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())
 
 
n, m, q = arr()
parent = [i for i in range(n + 1)]
size = [1] * (n + 1)
 
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
 
def union(x, y):
    parx = find(x)
    pary = find(y)
    if parx == pary:
        return
    if size[parx] < size[pary]:
        parent[parx] = pary
        size[pary] += size[parx]
    else:
        parent[pary] = parx
        size[parx] += size[pary]
 
edges = set()
for _ in range(m):
    u, v = arr()
    if u > v:
        u, v = v, u
    edges.add((u, v))
 
ops = []
used_edges = set()
for _ in range(q):
    parts = input().split()
    t, u, v = parts[0], int(parts[1]), int(parts[2])
    if u > v:
        u, v = v, u
    ops.append((t, u, v))
    if t == 'cut':
        used_edges.add((u, v))
 
for (u, v) in edges:
    if (u, v) not in used_edges:
        union(u, v)
 
ans = []
for op in reversed(ops):
    t, u, v = op
    if t == 'ask':
        ans.append("YES" if find(u) == find(v) else "NO")
    else:  
        union(u, v)
 
for res in reversed(ans):
    print(res)