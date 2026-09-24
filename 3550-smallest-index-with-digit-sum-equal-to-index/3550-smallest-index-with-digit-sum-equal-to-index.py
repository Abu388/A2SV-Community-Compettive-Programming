class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            

            n = str(nums[i])
            val = 0
            for j in n:
                val += int(j)

            if val == i:
                return i
        return -1
        