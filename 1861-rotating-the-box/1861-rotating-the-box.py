class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        for r in range(len(boxGrid) - 1, -1 , -1):
            for c in range(len(boxGrid[0]) - 1, -1, -1):
                if boxGrid[r][c] == "#":
                    t = c # shifted into the right  col// 
                    while t + 1 < len(boxGrid[0]) and boxGrid[r][t + 1] == ".":
                        boxGrid[r][t] , boxGrid[r][t + 1] = boxGrid[r][t + 1] ,boxGrid[r][t]
                        t += 1
        
        arr = [[0] * len(boxGrid) for _ in range(len(boxGrid[0]))]
        row = col = 0
        for r in range(len(boxGrid) -1, -1, -1):
            row = 0
            for v in boxGrid[r]:
                arr[row][col] = v
                row += 1
            col += 1 
        return arr