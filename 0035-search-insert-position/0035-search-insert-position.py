class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for n, i in enumerate(nums):
            if target == i:
                return n
        z=0
        val=0

    
        while z<len(nums) :
            if nums[z]< target:
                val=z+1
            z+=1
        return val
        