# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum=max(nums)
        cur=0
        arr=[]
        
        for i in nums:
            cur+=i
            maximum=max(cur,maximum)
            if cur<0:
                cur=0
            
        return maximum
  

