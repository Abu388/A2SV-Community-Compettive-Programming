class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = [0] * len(grid)
        col = [0] * len(grid[0])
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    row[r] += 1
                    col[c] += 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and max(row[r],col[c] ) > 1:
                    count += 1
                    
        return count

