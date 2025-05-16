# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        maxs = 1
        for i in range(len(nums)):
            c = 1
            curr = nums[i]
            for j in range(i+1, len(nums)):
                if curr & nums[j] == 0:
                    curr |= nums[j]
                    c += 1
                    maxs = max(c, maxs)
                else:
                    break
        return maxs
