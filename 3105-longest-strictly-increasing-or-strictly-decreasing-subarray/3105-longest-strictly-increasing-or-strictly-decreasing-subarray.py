class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        res = 1
        c = 1
        for i in range(1,len(nums)):
            if nums[i - 1] < nums[i]:
                c += 1
            else:
                res = max(c, res)
                c = 1
        res = max(c, res)
        c = 1
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                c += 1
            else:
                res = max(c, res)
                c = 1
            
        res = max(c, res)
        return res


        
            
            
       