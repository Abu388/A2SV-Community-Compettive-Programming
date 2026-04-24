class Solution:
    def minCost(self, n: int) -> int:
        if n == 1:
            return 0
        res = 0
        b , a = n - 1 , 1
        while a != b:
            res += b
            b -= 1
        return res + 1
