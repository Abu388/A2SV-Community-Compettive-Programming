# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        nums = []
        cost = 0
        
        for num in instructions:
            less = bisect_left(nums, num)
            greater = len(nums) - bisect_right(nums, num)
            cost += min(less, greater)
            insort(nums, num)  
        return cost % MOD
