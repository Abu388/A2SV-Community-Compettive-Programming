class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 3:
            if 0 not in nums:
                return 0
            if 1 not in nums:
                return 1 
            return -1
        count = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                count += 1
                for j in range(i, i + 3):
                    nums[j] = 1 if nums[j] == 0 else 0
                   

        return count if 0 not in nums else -1
