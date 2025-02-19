# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix=[0]*(len(nums)+1)
        n_prefix=[]
        prev=0
        res=0

        for start,end in requests:
            prefix[start]+=1
            prefix[end+1]-=1
        prefix.pop()
        for i in prefix:
            prev+=i
            n_prefix.append(prev)
        n_prefix.sort()
        nums.sort()
        for j in range(len(n_prefix)):
            res+=(nums[j]*n_prefix[j])
        return res%(10**9 + 7)
