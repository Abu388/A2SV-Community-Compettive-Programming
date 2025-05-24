# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        q = deque()
        count = 0
        def inbond(r,c):
            return 0 <= r < len(grid) and 0  <= c < len(grid[0])
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        flag = True
        for  i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i,j))
                    
                    while q:
                        
                        for _ in range(len(q)):
                            r , c = q.popleft()
                            visited.add((r,c))
                            for nr , nc in d:
                                newr = r + nr
                                newc = c + nc 
                                if not inbond(newr,newc) or grid[newr][newc] == 0 :
                                    count += 1
                                elif grid[newr][newc] == 1 and (newr,newc) not in visited:
                                    q.append((newr,newc))
                                    visited.add((newr,newc))         
                                 
                    return count