# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]: 
        q = deque([])  
        visited = set()                                               
        d  = [(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(row , col):
            return 0 <= row < rows and 0 <= col < cols


        rows = len(mat)
        cols = len(mat[0])
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:                                     
                    q.append((row,col))
                    visited.add((row,col))
                else:
                    mat[row][col] = 'b'
                


                 
        while q:
            r, c = q.popleft()
            for nr , nc in d:
                newr = r + nr
                newc = c + nc
                if inbound(newr,newc):
                    if mat[newr][newc] == 'b' and (newr,newc) not in visited:
                        q.append((newr,newc))
                        visited.add((newr,newc))
                        mat[newr][newc] = mat[r][c] + 1

                    
    

                      
        
        return mat