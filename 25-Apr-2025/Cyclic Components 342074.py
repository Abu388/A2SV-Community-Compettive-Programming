# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

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
 
 
def dfs (node):
    global cycle
    if len(graph[node]) != 2  and len(graph)>= 3:
        cycle = False
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            dfs(neighbor)
 
 
 
ans = 0
visited = set()
n , m = arr()
graph = defaultdict(list)
for _ in range(m):
    u , v = arr()
    graph[u].append(v)
    graph[v].append(u)
 
for i in range(1, n + 1):
        if i not in visited and i in graph:
            visited.add(i)
            cycle = True
            dfs(i)
            if cycle :
                ans += 1
 
print(ans)