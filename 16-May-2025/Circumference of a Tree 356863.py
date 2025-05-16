# Problem: Circumference of a Tree - https://codeforces.com/gym/102694/problem/A


from collections import deque
import sys


input = sys.stdin.readline

def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())

n = test()
def bfs(k):
    q = deque([k])
    visited = [0] * (n+1)
    visited[k] = 1
    d = 0
    last = 0
    while q:
        for _ in range(len(q)):
        
            last = c = q.popleft()

            for negh in graph[c]:
                if not visited[negh]:
                    q.append(negh)
                    visited[negh] = 1
        d += 1
    return (d,last)

graph = [[] for _ in range(n+1)]
if n ==  1:
    print(0)
else:
    for _ in range(n-1):
        u , v = arr()
        graph[u].append(v)
        graph[v].append(u)
    
    first =bfs(1)[1]
    d = bfs(first)[0]
   
        
    print((d-1)*3)
        







