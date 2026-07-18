from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m = max(nums)
        n = min(nums)
        return gcd(n,m)