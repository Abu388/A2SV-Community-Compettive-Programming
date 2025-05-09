# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        parent = [i for i in range(m * n)]
        size = [1] * (m * n)

        def find(x):
            stk  = []
            while parent[x] != x:
                stk.append(x)
                x = parent[x]        
            while stk:
                parent[stk.pop()] = x
            return parent[x]

        def union(x, y):
            xu = find(x)
            yu = find(y)
            if xu == yu:
                return
            if size[xu] > size[yu]:
                size[xu] += size[yu]
                parent[yu] = xu
            else:        
                size[yu] += size[xu]
                parent[xu] = yu

        directions = {
            'left':  (0, -1),
            'right': (0, 1),
            'up':    (-1, 0),
            'down':  (1, 0)
        }

        street_map = {
            1: ['left', 'right'],
            2: ['up', 'down'],
            3: ['left', 'down'],
            4: ['right', 'down'],
            5: ['left', 'up'],
            6: ['right', 'up'],
        }

        opposite = {
            'left': 'right',
            'right': 'left',
            'up': 'down',
            'down': 'up'
        }

        def idx(r, c):
            return r * n + c

        for r in range(m):
            for c in range(n):
                for d in street_map[grid[r][c]]:
                    print(d)
                    dr, dc = directions[d]
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if opposite[d] in street_map[grid[nr][nc]]:
                            union(idx(r, c), idx(nr, nc))

        return find(0) == find(m * n - 1)