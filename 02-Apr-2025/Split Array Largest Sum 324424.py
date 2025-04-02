# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

from itertools import accumulate
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r= sum(nums)
        def valid(mid,m):
            rsum = 0
            val = 0
            for num in nums:
                rsum += num
                if rsum > mid:
                    val += 1
                    rsum = num

            return val+1 <= m
        
        while l<=r:
            mid = (l+r)//2
            if valid(mid,k):
                r = mid - 1
            else:
                l = mid + 1
        return l