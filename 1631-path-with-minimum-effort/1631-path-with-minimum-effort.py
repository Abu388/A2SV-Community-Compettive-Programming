class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0, 0 ,0 )]  # count , row , col
        row , col = len(heights) - 1, len(heights[0]) - 1
        def inbound(r, c):
            return 0 <= r < len(heights) and 0 <= c < len(heights[0]) 
        visited = set()
        heapq.heapify(heap)
        direction = [(0, 1), (1, 0), (-1 , 0) , (0, -1)]
    
        
        while heap:
            w , r , c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            visited.add((r,c))
            if r == row and c == col:
                return w
                
            for dr , dc in direction:
                nr = r + dr
                nc = c + dc
                if inbound(nr , nc) and (nr,nc) not in visited:
                    val = heights[r][c] - heights[nr][nc]
                    val = max(w , abs(val))
                    heapq.heappush(heap , (val, nr , nc ))
            
     