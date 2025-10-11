# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stk = deque([])
        res = 0
        for w in s:
            if not stk:
                stk.append(w)
            else:
                while w in stk:
                    print(stk)
                    stk.popleft()
                stk.append(w)
            res = max(res, len(stk))
        return res
            
