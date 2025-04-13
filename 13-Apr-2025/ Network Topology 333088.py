# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

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
def dfs(graph,n,m):
    #chake for bus only the first and the final have only one value
    f= len(graph[1])
    s= len(graph[n])
    flag = True
    ring = True
    if f == 2 and s == 2:
        for i in range(1,n+1):
            
            if len(graph[i]) != 2:
                ring = False
                break
        if ring:return "ring topology"
    count = 0
    cm = 0
    for i in range(1,n+1):
        if len(graph[i]) ==  1:
            count += 1
        elif len(graph[i])  ==  m:
            cm += 1
    if cm == 1 and (n-count) == 1:
        return "star topology"
    
    for i in range(1,n+1):
        if len(graph[i]) != 2 and len(graph[i]) != 1:
            flag = False
            break
    if flag:
        return "bus topology"
    return "unknown topology"


n , m = arr()
visited = set()
graph = defaultdict(list)
for   i in range(1,n+1):
    visited.add(i)
for _ in range(m):
    l , r = arr()
    graph[l].append(r)
    graph[r].append(l)

    if l in visited:
        visited.remove(l)
    if r in visited:
        visited.remove(r)


if len(visited) > 0:
    
    print("unknown topology")
else:
    print(dfs(graph,n,m))

    
