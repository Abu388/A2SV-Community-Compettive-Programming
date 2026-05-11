class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1 and s2 == s3:
            return True
        if not s2 and s1 == s3:
            return True
        if not s1 and not s2 and not s3:
            return True
        grid = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]
        grid[0][0] = True
        col , row = len(grid[0]) , len(grid) 
        l = 0
        for c in range(1, col):
            if s3[l] == s1[l]:                
                grid[0][c] = grid[0][c - 1]
            else: 
                grid[0][c] = False
            l += 1
        l = 0
        for r in range(1, row):
            if s3[l] == s2[l]:
                grid[r][0] = grid[r - 1][0]
            else: 
                grid[r][0] = False
            l += 1
        
        for r in range(1,row):
            loc = r - 2
            for c in range(1,col):
                loc = r + c - 1
                grid[r][c] = (
                                (s1[c - 1] == s3[loc] and grid[r][c - 1]) or
                                (s2[r - 1] == s3[loc] and grid[r - 1][c])
                            )

                loc += 1


        return grid[row - 1][col - 1]