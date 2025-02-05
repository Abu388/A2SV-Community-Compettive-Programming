# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        has={}
        res=[]
        for i in nums:
            has[i]=has.get(i,0)+1
        checker=len(nums)//3
        for keys, values in has.items():
            if values>checker:
                res.append(keys)
        return res

