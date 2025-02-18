# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mp={0:1}
        rsum=0
        ans=0
        for i in nums:
            rsum+=i
            if rsum-goal in mp:
                ans+=mp[rsum-goal]
            mp[rsum]=mp.get(rsum,0)+1
        return ans