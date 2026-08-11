class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = set(nums)
        for j in range(1, len(nums)):
            if nums[j] == nums[j - 1] + 1:
                continue
            val = nums[:j]
            x = sum(val)
            while x in s:
                x += 1
            return x
        x = sum(nums)

        while x in s:
            x += 1

        return x


        