class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            res += nums[len(nums) - 1] - nums[i]
        return res