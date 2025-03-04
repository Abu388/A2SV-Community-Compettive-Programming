# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

from collections import Counter
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        s=list(s)
        
        for i in range(len(s)):
            if s[i] == 'R':
                s[i]=1
            else:
                s[i]=-1
        for i in range(1,len(s)):
            s[i]+=s[i-1]
        return s.count(0)
        
        