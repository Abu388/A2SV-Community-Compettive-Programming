# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        final = [[0]*cols for _ in range(rows)]
        d = [(-1,0),(0,-1),(1,0),(0,1)]
        def valid(r,c): return 0<= r <rows and 0<= c < cols

        def dfs(r,c):
            if final[r][c] != 0:
                return final[r][c]
            count = 1
            for nr , nc in d:
                newr , newc = nr + r , nc + c
                if valid(newr,newc):
                    if matrix[newr][newc] > matrix[r][c]:
                        count = max(count,1+dfs(newr,newc))
            final[r][c] = count
            return count

        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res,dfs(r,c))
                
        return res
        

