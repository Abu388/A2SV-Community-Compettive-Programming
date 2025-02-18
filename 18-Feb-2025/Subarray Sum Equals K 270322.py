# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        rsum , n= 0, len(nums)
        mp[0] = 1
        ans = 0
        for i in range(n):
            rsum+=nums[i]
            if mp[rsum-k]>0:
                ans+=mp[rsum-k]
            mp[rsum]+=1
        
        return ans
       