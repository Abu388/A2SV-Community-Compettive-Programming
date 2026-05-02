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
                    
                    stk.popleft()
                stk.append(w)
            res = max(res, len(stk))
        return res