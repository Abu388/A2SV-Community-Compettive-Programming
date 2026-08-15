class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^=  nums[i] 
        if res > 0 :
            return len(nums)
        # FRONT PART
        f = res
        b = res
        f_res , b_res = 0, 0
        for i in range(len(nums)):
            f ^= nums[i]
            if f > 0 :
                f_res = len(nums) - i - 1
                break 
        #for back
        for i in range(len(nums) - 1, - 1 , -1):
            b ^= nums[i] 
            if f > 0 :
                b_res = i 
                break 
        return max(f_res,b_res)

        

        