# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # collect one and move into 4 directions 
        # create direction, inbound , qeue , visited 
        m = len(grid) # row
        n = len(grid[0]) # col
        visited = set()
        dire = [(0,1),(0,-1),(1,0),(-1,0)]
        q = deque([])
        count = 0
        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n
        def island(q):
            nonlocal count
            while q:
                r , c = q.popleft()
                for nr , nc in dire:
                    row = nr + r
                    col = nc + c
                    if inbound(row, col) and (row, col) not in visited:
                        if grid[row][col] == '1':
                            q.append((row,col))
                            visited.add((row,col))
            
            count += 1 #one island is done

        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == '1':
                    q.append((i,j))
                    island(q)
        
        return count

    
      

      
    

    
    

    