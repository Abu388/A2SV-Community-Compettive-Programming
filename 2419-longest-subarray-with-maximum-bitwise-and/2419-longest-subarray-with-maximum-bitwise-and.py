class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans,count=0,0
        val=float("-inf")
        for i in nums:
            val=max(i,val)
        for j in nums:
            if j == val:
                count+=1
            else:
                count=0
            ans=max(count,ans)
            
        return ans
