class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len((nums))):
            if nums[i] < 0:
                nums[i] = -1 * nums[i]
        nums.sort()
        if len(nums) % 2 == 0:
            l , r = 0, len(nums) - 1
            while l <= r:
                res += ( (nums[r] ** 2) - (nums[l] ** 2) )
                l += 1
                r -= 1 
        else:
            l , r = 0, len(nums) - 1
            while l <= r:
                res += ( (nums[r] ** 2) - (nums[l] ** 2) )
                l += 1
                r -= 1 
            res += nums[len(nums) // 2] ** 2
        return res

        