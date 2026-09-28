class Solution:
    def maxDepth(self, s: str) -> int:
        stk = []
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stk.append('(')
            
            if s[i] == ')':
                res = max(res, len(stk))
                stk.pop()
        return res