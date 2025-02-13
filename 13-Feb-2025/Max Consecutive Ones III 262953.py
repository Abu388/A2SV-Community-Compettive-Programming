# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        r=0
        l=0
        res=0
        while r<len(nums):
            if nums[r]==0:
                k-=1
            r+=1

            
            
            while k <0:
                 
                if nums[l]==0:
                    k+=1
                l+=1
            res=max(res,r-l)
        return res