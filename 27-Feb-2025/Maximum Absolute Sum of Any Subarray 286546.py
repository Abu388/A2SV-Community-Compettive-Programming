# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        max_sum = float('-inf')  
        min_sum=float('inf')
        current_sum = 0
        
        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0 

        curr=0
        for i in nums:
            curr += i
            min_sum=min(curr,min_sum)
            if curr>0:
                curr=0
            
        return max(abs(max_sum),abs(min_sum))


     