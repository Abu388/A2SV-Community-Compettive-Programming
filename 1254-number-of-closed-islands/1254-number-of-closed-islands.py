class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        direction = [(0,1),(1,0),(-1,0),(0, -1)]
        def inbound(r,c):
            return 0<= r < len(grid) and  0<= c < len(grid[0])
        def corner(r,c):
            return 0 == r or r == len(grid) - 1 or  0 == c or c == len(grid[0]) - 1
        def bfs(row,col):
            q = deque([(row,col)])
            grid[row][col] = 1 
            flag = True
            while q:
                r , c = q.popleft()
                if corner(r,c):
                    flag = False
                for dr , dc in direction:
                    nr = dr + r
                    nc = dc + c
                    if inbound(nr,nc) and grid[nr][nc] == 0:                        
                        grid[nr][nc] = 1                        
                        q.append((nr,nc))

            return flag
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    if bfs(r,c):
                        count += 1

        return count




        