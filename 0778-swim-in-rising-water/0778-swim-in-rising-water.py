class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        direction = [(1,0),(0,1),(-1, 0) ,(0,-1)]
        heap = [(grid[0][0], 0 , 0)] # cost , r , c
        visited = set()
        def inbound(r, c ):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        while heap:
            cost , r , c = heapq.heappop(heap)
            
            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return cost
            
            for dr , dc in direction:
                nr , nc = r + dr , c + dc
                if inbound(nr, nc):
                    new_c = max(cost , grid[nr][nc] )
                    heapq.heappush(heap, (new_c, nr, nc))

        
                 