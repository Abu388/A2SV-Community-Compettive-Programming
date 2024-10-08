class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l=len(nums)-1
        while l>0:
            for i in range(l):
                if -nums[i]== nums[l]:
                    return nums[l] 
                    
                    
            l-=1
        return -1