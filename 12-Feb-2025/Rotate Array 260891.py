# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        
            

        for ind,i in enumerate(nums[::-1]):
            nums[ind]=i
        last=nums[:k]
        start=nums[k:]
    
        
        for index , val in enumerate(last[::-1]):
            nums[index]=val
            
        for j,v in enumerate(start[::-1]):
            nums[k+j]=v




       
    
       
      

            
            
       
        


        
        