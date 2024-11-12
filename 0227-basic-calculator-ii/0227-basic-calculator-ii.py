class Solution:
    def calculate(self, s: str) -> int:
       
        l = [c for c in s]  
        stack = []
        num = 0
        op = '+'
        r = 0

        while r < len(s):
            if s[r].isdigit():
                num = num * 10 + int(s[r])
            if s[r] in "+-*/" or r == len(s) - 1: 
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))  
                op = s[r]  
                num = 0
            r += 1
        return sum(stack)
        

        