class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        fin=[0]*(len(nums))
        l=0
        for i in range(len(nums)):
            if nums[i] !=0:
                fin[l]=nums[i]
                l+=1

                
        return fin