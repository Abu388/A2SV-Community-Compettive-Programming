class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return abs(nums[0] - nums[1])
        res = 0
        
        m = (len(nums) // 2) 
        val = nums[m]
        for i in range(m):
            res += val - nums[i]
        
        for i in range(m + 1, len(nums)):
            res += nums[i] - val
        return res
    

 