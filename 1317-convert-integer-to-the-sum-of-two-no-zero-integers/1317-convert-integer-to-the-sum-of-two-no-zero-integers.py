class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            if "0" not in f"{i}{n-i}":
                return [i,n-i]