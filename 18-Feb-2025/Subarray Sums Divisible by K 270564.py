# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp=defaultdict(int)
        mp[0]=1
        rsum=0
        ans=0
        for num in range(len(nums)):
            rsum+=nums[num]
    
     
            ans+=mp[rsum%k] 
            mp[rsum%k]+=1
        return ans
                

        