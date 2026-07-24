class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res = []
        for s in matrix:
            res.append(sum(s))
        return res
        