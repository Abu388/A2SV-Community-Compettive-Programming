class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row , col = len(grid) - 1, len(grid[0]) - 1
        def inbound(r , c):
            return  0 <= r <= row and 0 <= c <= col
        def bord(r , c) :
            return 0 == r or c == 0 or c == col or r == row
        
        def dfs(r ,c):
            if not inbound(r ,c) or grid[r][c] == 0 or (r , c ) in visited :
                return
            visited.add((r , c))
            
            dfs(r + 1 , c)
            dfs(r - 1 , c)
            dfs(r , c + 1)
            dfs(r , c - 1)

        visited = set()
        for r in range(row + 1):
            for c in range(col + 1):
                if bord(r,c) and (r , c) not in visited and grid[r][c] == 1:
                    dfs(r ,c)
        count = 0
        for r in range(row + 1):
            for c in range(col + 1):
                if (r , c ) not in visited and grid[r][c] == 1:
                    count += 1
        return count