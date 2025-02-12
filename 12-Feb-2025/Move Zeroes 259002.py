# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        p=0
        s=0
        while s<len(nums):
            if nums[s]!=0:
                nums[p],nums[s]=nums[s],nums[p]
                p+=1
            s+=1
            
        