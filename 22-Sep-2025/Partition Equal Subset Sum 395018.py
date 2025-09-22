# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        mp = defaultdict(tuple)
       
        tot = sum(nums)
        if tot % 2:
            return False
        half = tot // 2

        def solu(n , val):
            nonlocal half
            if n >= len(nums) or val > half:
                return False
            if half == val:
                return True
            if (n , val )  in mp:
                return mp[(n, val)]
            

            mp[(n , val)] =solu(n + 1 , val + nums[n]) or solu(n + 1, val)
              
            return mp[(n , val)]
            
        return solu(0 , 0)

        