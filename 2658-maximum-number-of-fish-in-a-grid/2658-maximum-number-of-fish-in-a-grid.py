class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        visited = set()
        def dfs(r, c):
            
            if not inbound(r,c) or grid[r][c] == 0 or (r,c)  in visited:
                return 0
            visited.add((r,c))
            f = grid[r][c]      
            f += dfs(r + 1, c) 
            f += dfs(r, c + 1)
            f += dfs(r - 1 , c)
            f += dfs(r, c - 1)
            return f
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0 and (r,c) not in visited:
                    res = max(res,dfs(r , c))

        return res
