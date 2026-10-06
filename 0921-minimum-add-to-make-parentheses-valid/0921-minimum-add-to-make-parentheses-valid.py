class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = [] 
        c = 0
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(s[i])
            else:
                if not stk:
                    c += 1
                else:
                    stk.pop()
        return c + len(stk)

        
        