# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        l=0
        r=0
        res=float("inf")
        count=0

        while r<len(nums):
            while count<target and r<len(nums):
                count+=nums[r]            
                r+=1
            while count>=target and l<len(nums):
                res=min(res,r-l)              
                count-=nums[l]
                l+=1    
                

        return res
            
            
                
                
                

                
                
                
            
        
        