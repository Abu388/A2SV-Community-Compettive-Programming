# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

import sys
from collections import deque

def solve():
    n = int(sys.stdin.readline())
    names = [sys.stdin.readline().strip() for _ in range(n)]
    
    graph = {chr(ord('a') + i): [] for i in range(26)}
    in_degree = {chr(ord('a') + i): 0 for i in range(26)}
    
    for i in range(n - 1):
        name1 = names[i]
        name2 = names[i + 1]
        found = False
        for c1, c2 in zip(name1, name2):
            if c1 != c2:
                graph[c1].append(c2)
                in_degree[c2] += 1
                found = True
                break
        if not found and len(name1) > len(name2):
            print("Impossible")
            return
    
    queue = deque()
    for c in in_degree:
        if in_degree[c] == 0:
            queue.append(c)
    
    topo_order = []
    while queue:
        if len(queue) > 1:
           
            pass
        u = queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    if len(topo_order) != 26:
        print("Impossible")
    else:
        print(''.join(topo_order))

solve()