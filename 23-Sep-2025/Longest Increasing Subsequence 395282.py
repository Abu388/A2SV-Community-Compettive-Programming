# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        memo = defaultdict(int)
        def soul(i):
            if i in memo:
                return memo[i]
            ma = 0 
            for j in range(i + 1, len(nums) ):
                if nums[ j ] > nums[ i ]:
                    ma = max(soul(j), ma)
            memo[i] = ma + 1 
            return memo[i] 

        for i in range(len(nums)):
            res = max(res , soul(i))
        return res   

