# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        total = 0
        local = 0

        for i in s:
            if i == '(':
                stk.append(local)
                local = 0  
            else:
                local = max(2 * local, 1)  
                local += stk.pop()  

        return local
                



        
            