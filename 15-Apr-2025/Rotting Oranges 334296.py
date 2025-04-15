# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

from collections import deque
from typing import List  # needed if you're using List in type hints

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        one = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col, 0))  
                elif grid[row][col] == 1:
                    one += 1

        m = 0
        visited = set()

        while q:
            r, c, minute = q.popleft()
            visited.add((r, c))
            m = max(m, minute)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1 and (nr, nc) not in visited:
                        grid[nr][nc] = 2
                        visited.add((nr, nc))
                        q.append((nr, nc, minute + 1))
                        one -= 1

        return m if one == 0 else -1
