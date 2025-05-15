# Problem: E - Cycle in Graph - https://codeforces.com/gym/602812/problem/E

import sys
import threading
from collections import defaultdict

# Increase the recursion limit and stack size to handle deep DFS
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)


def main():
    def solve():
        # Read number of nodes (n), number of edges (m), and minimum cycle length (k)
        n, m, k = map(int, sys.stdin.readline().strip().split())

        # Build the undirected graph as an adjacency list
        graph = defaultdict(list)
        for _ in range(m):
            u, v = map(int, sys.stdin.readline().strip().split())
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        path_stack = []

        # Depth-First Search to find a cycle of length > k
        def dfs(current, parent):
            visited.add(current)
            path_stack.append(current)

            for neighbor in graph[current]:
                if neighbor == parent:
                    continue
                if neighbor not in visited:
                    dfs(neighbor, current)
                else:
                    # A back edge found, which indicates a cycle
                    if neighbor in path_stack:
                        cycle_start_index = path_stack.index(neighbor)
                        cycle = path_stack[cycle_start_index:]
                        if len(cycle) > k:
                            print(len(cycle))
                            print(*cycle)

                            # Exit the program immediately after finding the valid cycle
                            sys.exit(0)

            path_stack.pop()

        # Start DFS from node 1
        dfs(1, -1)

    solve()


# Run the main function in a new thread to support increased stack size
if __name__ == "__main__":
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()