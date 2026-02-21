class Solution:
    def nearestExit(self, grid: List[List[str]], entrance: List[int]) -> int:
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        def exite(r,c):
            return 0 == r or r == len(grid) -1 or c == 0 or c == len(grid[0]) -1
        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        def bfs(row,col):
            q = deque([(row, col , 0)])
            visited.add((row,col))
            
            while q:
                r , c , num = q.popleft()
                if exite(r,c) and (r,c) != (entrance[0], entrance[1]) :
                    return num
                for dr , dc in direction:
                    nr = dr + r
                    nc = dc + c
                    if inbound(nr,nc) and grid[nr][nc] == '.' and (nr,nc) not in visited :
                        q.append((nr , nc , num + 1))
                        visited.add((nr,nc))
            return -1




        
        return bfs(entrance[0], entrance[1])
            