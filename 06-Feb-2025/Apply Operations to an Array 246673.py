# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        res=[0]*len(nums)
        ind=0
        for j in range(len(res)):
            if nums[j] !=0:
                res[ind]=nums[j]
                ind+=1
        return res

