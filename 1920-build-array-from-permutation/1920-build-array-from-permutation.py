class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        l = 0
        while l < len(nums):
            arr[l] = nums[nums[l]]

            l += 1
        return arr