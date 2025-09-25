# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        memo = defaultdict(int)
        def solu(i , val):
            
            add = sub = 0
            if (i , val) in memo:
                return memo[(i,val)]
            if i == len(nums)  and val == 0:
                return 1

            if i < len(nums):
                # print(i)
                sub = solu(i + 1 , val - nums[i ])
                add = solu(i + 1,  val + nums[i ])
            memo[(i , val )] = add + sub

            return add + sub
        
        return solu(0 , target )

