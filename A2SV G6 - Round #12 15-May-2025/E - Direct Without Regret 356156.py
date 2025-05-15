# Problem: E - Direct Without Regret - https://codeforces.com/gym/606404/problem/E

from collections import deque
import sys

input = sys.stdin.readline
read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split()))

def solve():
    n, m = read_ints()
    directed_edges = []
    undirected_edges = []

    adjacency_list = [[] for _ in range(n)]
    in_degree = [0] * n

    for _ in range(m):
        edge_type, u, v = read_ints()
        u -= 1
        v -= 1
        if edge_type == 1:
            directed_edges.append((u + 1, v + 1))
            adjacency_list[u].append(v)
            in_degree[v] += 1
        else:
            undirected_edges.append((u, v))

    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    topo_order = []
    while queue:
        current = queue.popleft()
        topo_order.append(current)
        for neighbor in adjacency_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) < n:
        print("NO")
        return

    print("YES")
    position_in_topo = [0] * n
    for i, node in enumerate(topo_order):
        position_in_topo[node] = i

    for u, v in undirected_edges:
        if position_in_topo[u] < position_in_topo[v]:
            print(u + 1, v + 1)
        else:
            print(v + 1, u + 1)
    for u, v in directed_edges:
        print(u, v)

for _ in range(read_int()):
    solve()