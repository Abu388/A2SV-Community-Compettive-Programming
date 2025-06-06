# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums=list(map(str,nums))
        
        nums.sort(key=lambda x:x*10  , reverse=True)

        if nums[0]== '0':
            return '0'
        return ''.join(nums)
        
