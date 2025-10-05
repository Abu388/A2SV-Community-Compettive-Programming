# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(val):
            c = 0
            if val == target:
                return 1

            if val > target:
                return 0
            
            for j in nums:
                c += dp(val + j)
            return c
        return dp(0)