# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

from itertools import accumulate # to work on prefix

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prifix = list(accumulate(nums))
        total = 0
        sufix = []
        for i in range(len(nums)-1,-1,-1):
            total += nums[i]
            sufix.append(total)
        sufix = sufix[::-1]
      
        for i in range(len(nums)):
            if prifix[i] == sufix[i]:
                return i
        return -1
        