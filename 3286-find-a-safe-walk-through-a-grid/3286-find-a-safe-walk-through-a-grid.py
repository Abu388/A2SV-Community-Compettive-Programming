class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0]) 
        direction = [(1,0),(0,1),(0,-1),(-1,0)]
        heap = [(-health if grid[0][0] == 0 else -health + 1,0,0)]
        visited = set()
        while heap:
            h, r , c  = heapq.heappop(heap)
            if (r,c) in visited or h >= 0:
                continue
            if r == len(grid) - 1  and c == len(grid[0]) - 1:

                return True
            visited.add((r,c))
            for dr, dc in direction:
                nr = dr + r
                nc = dc + c
                if inbound(nr,nc) and (nr,nc) not in visited:
                    if grid[nr][nc] == 1:
                        heapq.heappush(heap,(h + 1, nr, nc))
                    else:
                        heapq.heappush(heap,(h , nr, nc))
        return False











        


        