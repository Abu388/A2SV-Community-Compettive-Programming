# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        has={}
        for i in nums:
            has[i]=has.get(i,0)+1
        for keys ,values in has.items():
            if values == 2:
                res.append(keys)
        return res