class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        s = nums[0]
        l = nums[len(nums) - 1]
        res = []
        val = set(nums)
        for i in range(s,l ):
            if i not in val:
                res.append(i)
            
        return res

        