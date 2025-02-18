# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.r=len(self.matrix)
        self.c=len(self.matrix[0])
        self.prifix=[[0]*self.c for _ in range(self.r)]
        for i in range(self.r):
            for j in range(self.c):
                self.prifix[i][j]=self.matrix[i][j]
                if i>0:
                    self.prifix[i][j]+=self.prifix[i-1][j]
                if j>0:
                    self.prifix[i][j]+=self.prifix[i][j-1]
                if i>0 and j>0:
                    self.prifix[i][j]-=self.prifix[i-1][j-1]

        
    def in_bound(self, x, y):
        return (0 <= x < self.r) and (0 <=y <self.c)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top_region = self.prifix[row1-1][col2] if self.in_bound(row1-1, col2) else 0
        left_region =self.prifix[row2][col1-1] if self.in_bound(row2, col1-1) else 0
        inter_region = self.prifix[row1-1][col1-1] if self.in_bound(row1-1, col1-1) else 0

        return self.prifix[row2][col2] - top_region - left_region + inter_region
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)