# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        def solu(n):
            if n == 0:
                return nums[0]
            if n == 1:
                return max(nums[0],nums[1])
            if n not in mp:
                mp[n] = max(solu(n - 1), solu(n - 2) + nums[n])
            return mp[n]
      

        return solu(len(nums) - 1)