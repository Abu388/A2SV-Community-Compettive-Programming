# Problem: D - Chasing Letters in a Graph - https://codeforces.com/gym/606404/problem/D

import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    s = "9" + sys.stdin.readline().strip()  # 1-based indexing: add dummy char

    graph = defaultdict(list)
    degree = [0] * (n + 1)  # in-degree of each node

    # Build the graph and count in-degrees
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        degree[b] += 1

    stack = []       # to process nodes with in-degree 0
    visited = []     # track the order of processed nodes
    max_value = 0    # final result

    # count[i][c] = max number of times character c can appear on any path ending at node i
    count = [[0] * 26 for _ in range(n + 1)]

    # Start with nodes that have no incoming edges
    for node in range(1, n + 1):
        if degree[node] == 0:
            stack.append(node)
            visited.append(node)

    # Process the graph in topological order
    while stack:
        node = stack.pop()

        # Count the current node's letter
        count[node][ord(s[node]) - ord('a')] += 1

        # Update the result if this path has a higher value
        max_value = max(max_value, max(count[node]))

        # Pass the stored information to children
        for neighbor in graph[node]:
            degree[neighbor] -= 1
            for c in range(26):
                count[neighbor][c] = max(count[neighbor][c], count[node][c])
            if degree[neighbor] == 0:
                stack.append(neighbor)
                visited.append(neighbor)

    # If not all nodes were visited, there's a cycle
    if len(visited) != n:
        print(-1)
    else:
        print(max_value)

solve()