class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        t = nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) - 3]
        b = nums[len(nums) - 1] * nums[0] * nums[1]
        return max(t,b)
        