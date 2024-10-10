class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l=len(nums)-1
        for i in range(l):
            if nums[i+1]-nums[i]>1:
                return nums[i]+1
            
        if nums[0] != 0:
            return 0
        else:
            return nums[l]+1
             
        
           
        
        