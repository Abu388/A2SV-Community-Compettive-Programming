class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        l=len(nums)-1
        while l>0:
            if nums[l]!=nums[l-1]:
                count+=(len(nums)-l) 
                
            l-=1
        return count 
        
        