class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        row = [0] * m
        col = [0] * n
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    row[r] += 1
                    col[c] += 1
        total = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1 and row[r] == 1 and col[c] == 1:
                    total += 1
        return total
