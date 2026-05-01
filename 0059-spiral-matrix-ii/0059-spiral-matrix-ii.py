class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0] * n for _ in range(n) ]
        
        top , bottom = 0 , n - 1
        left , right = 0 , n - 1
        c = 1
        while left <= right:
            for i in range(left, right + 1):
                grid[top][i] = c
                c += 1
            top += 1

            for i in range(top , bottom + 1):
                grid[i][right] = c
                c += 1
            right -= 1

            for i in range(right, left - 1, - 1):
                grid[bottom][i] = c
                c += 1
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                grid[i][left] = c
                c += 1
            left += 1

        return grid

            


