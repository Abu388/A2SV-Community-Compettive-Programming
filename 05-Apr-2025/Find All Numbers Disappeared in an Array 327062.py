# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums):
        res = []
        n = len(nums)
        i = 0
        while i < len(nums):
            c = nums[i]-1 
            if nums[i] != nums[c]:
                nums[i] , nums[c] = nums[c] , nums[i]
            else:
                i += 1
        
        for i in range(len(nums)-1,-1,-1):
            if n != nums[i]:
                res.append(n)
            n-=1


        return res
      