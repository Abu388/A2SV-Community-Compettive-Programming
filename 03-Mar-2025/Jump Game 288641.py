# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum=0
        for i in range(len(nums)):
            if i > maximum:
                return False
            maximum=max(maximum,nums[i]+i)     
            if maximum>= len(nums)-1:
                return True
        return True
            


        