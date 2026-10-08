class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stk = []
        d = 0
        for i in s:
            d += 1 if i == '(' else -1
            if (d == 1 and i == '(') or (d == 0 and i == ')'):continue
            stk.append(i)
            
        return "".join(stk)

        