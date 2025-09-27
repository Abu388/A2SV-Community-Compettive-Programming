# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
       
        l = 0
        c = 0
        for i in t:
            if l < len(s) and s[l] == i:
                c += 1
                l += 1
        return len(s) == c
