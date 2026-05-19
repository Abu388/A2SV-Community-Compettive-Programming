class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i not in memo:
                memo[i] = max(dp(i + 1), nums[i] + dp(i + 2))
            return memo[i]



        dp(0)
        return memo[0]
        
      
        
        
        
        # def dp(i):
        #     if i == 0:
        #         return nums[i]
        #     if i  == 1:
        #         return max(nums[1],nums[0])
        #     if i not in memo:
        #         memo[i] = max(dp(i - 1),dp(i - 2) + nums[i])
        #     return memo[i]

       
        # return dp(len(nums) - 1)