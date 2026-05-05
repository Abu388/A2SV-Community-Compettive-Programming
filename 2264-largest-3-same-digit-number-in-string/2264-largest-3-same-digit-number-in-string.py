class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9,-1 , -1):
            val = str(i) + str(i)  + str(i)
            if val in num:
                return val
        return ""