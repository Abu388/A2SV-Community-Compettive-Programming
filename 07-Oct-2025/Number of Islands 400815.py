# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # i have to start from (0,0 ) and i have supposet of go (m - 1, n - 1) BFS
        
        def inbound(row , col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def count(row , col):
            direction = [(0 , 1), (0 , - 1) ,( 1, 0), (-1 ,0)]
            checker = deque([(row , col)])
            visites.add((row , col))
            while checker:
                r , c = checker.popleft()
                for dr , dc in direction:
                    nr = r + dr
                    nc = c + dc
                    if inbound(nr , nc):
                        if (nr , nc) not in visites and grid[nr][nc] == '1':
                            visites.add((nr , nc))
                            checker.append((nr , nc))

            return 1

        
        result = 0
        visites = set()
        for r in range(len(grid)): # which is a row
            for c in range(len(grid[0])): # which is col
                if grid[r][c] == '1':
                    if (r , c) not in visites:                                               
                        result += count(r , c) 
        return result

    