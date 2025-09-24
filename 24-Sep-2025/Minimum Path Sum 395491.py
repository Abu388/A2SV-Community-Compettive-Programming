# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/


from collections import Counter, defaultdict,deque
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # i and j 
        memo = defaultdict(int)
        
        def bound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        

        def solu(row , col):
            down = right = float("inf")
            # print(row , col)
            if row == len(grid)-1 and col == len(grid[0]) -1:
                return grid[row][col]
            
            if (row,col) in memo:
                return memo[(row,col)]

            cur = grid[row][col]

            if bound(row , col + 1):
                #move to the right 
                right = cur + solu(row , col +  1)

            if bound(row + 1, col):
                #move down 
                down = cur + solu(row + 1 , col)

            res = min(right , down)
            memo[(row,col)] = res
            

            return res

        # solu(0,0)
        # print(memo)
        return solu(0,0)