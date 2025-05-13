# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        size = 4 * n * n
        parent = list(range(size))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for i in range(n):
            for j in range(n):
                root = 4 * (i * n + j)
                char = grid[i][j]

                if char == ' ':
                    union(root + 0, root + 1)
                    union(root + 1, root + 2)
                    union(root + 2, root + 3)
                elif char == '/':
                    union(root + 0, root + 3)
                    union(root + 1, root + 2)
                elif char == '\\':
                    union(root + 0, root + 1)
                    union(root + 2, root + 3)

                
                if i + 1 < n:
                    bottom = 4 * ((i + 1) * n + j)
                    union(root + 2, bottom + 0)
                if j + 1 < n:
                    right = 4 * (i * n + j + 1)
                    union(root + 1, right + 3)

        return sum(1 for i in range(size) if find(i) == i)
