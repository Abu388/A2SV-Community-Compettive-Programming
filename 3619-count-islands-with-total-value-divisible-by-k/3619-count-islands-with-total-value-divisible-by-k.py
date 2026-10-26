class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        def inbound(r,c):
            return 0<= r < len(grid) and 0 <= c < len(grid[0])
        q = deque()
        visited = set()
        res = 0
        def bfs(r,c):
            val = grid[r][c]
            q.append((r,c))
            visited.add((r, c))
            while q:
                row , col = q.popleft()
                for dr , dc in direction:
                    nr = dr + row
                    nc = dc + col
                    if inbound(nr,nc) and (nr,nc) not in visited:
                        if  grid[nr][nc] == 0:
                            continue
                        else:
                            val += grid[nr][nc]
                            q.append((nr,nc))
                            visited.add((nr,nc))
                        
            return val

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] != 0:
                    if bfs(i,j) % k == 0:
                        res += 1 
        return res