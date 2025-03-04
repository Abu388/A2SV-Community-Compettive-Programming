# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        has={0:-1}
        arr=[0]*len(nums)
        res=0
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        for i in range(len(nums)):
            if nums[i] not in has:
                has[nums[i]]=i
            else:
                res=max(res, i - has[nums[i]])
        return res



            


            
