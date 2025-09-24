# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        count = 0
        memo = defaultdict(int)
        if n == 1 and m == 1:
            return 1
        def bound(row,col):
            return 0 <= row < m and 0 <= col < n

        def solu(row , col):
            nonlocal count 
            val1 = val2 = 0
            if row == len(grid) -1 and col == len(grid[0]) -1:
                
                return 1
            if (row ,col) in memo:
                return memo[(row,col)]

            if bound(row , col + 1):
                #move to the right 
                val1 = solu(row , col +  1)

            if bound(row + 1, col):
                #move down 
                val2 = solu(row + 1 , col)
            memo[(row,col)] = val1 + val2

            return val1 + val2


        return solu(0,0)
        