class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        res=[]
        for ind, val in enumerate(nums):
            if val==target:
                res.append(ind)
        return res
        