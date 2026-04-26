class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l , r = 0, len(nums) - 1
        res = 0
        while l + 1 <= r:
            res += min(nums[l], nums[l + 1])
            l += 2
        return res
            