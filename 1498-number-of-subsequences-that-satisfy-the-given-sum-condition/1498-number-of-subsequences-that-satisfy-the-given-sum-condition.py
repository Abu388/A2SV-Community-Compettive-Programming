class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        res = 0

        r = n - 1
        for i , left in enumerate(nums):
            while (left + nums[r]) > target and i <= r:
                r -= 1
            if i <= r:
                res += (2**(r - i)) 
        
        
        return res % MOD
