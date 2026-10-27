class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
    
        row = m
        col = n
        grid = [ (['#'] * col)  for _ in range(row)]
        print(grid)
        for i in range(col):
            grid[0][i] = '.'
        print(grid)
        for j in range(row ):
            grid[j][col - 1] = '.'
        return ["".join(r) for r in grid]


    
