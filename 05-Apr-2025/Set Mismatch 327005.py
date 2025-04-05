# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

from collections import defaultdict
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mp = defaultdict(int)
        n = 1
       
        for i in nums:
            mp[i] += 1
        nums = set(nums)
        
        for k , v in mp.items():
            if v == 2:
                for i in nums:
                    if n != i:
                        return [k,n]
                    n += 1
                return [k,n]



