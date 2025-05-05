# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        
        for i in s:
            if i != ']':
                stk.append(i)
            else:
                res = ''
                while stk and stk[-1] != '[':
                    res = stk.pop() + res
                stk.pop()
                num = ''
                while stk and stk[-1].isdigit():
                    num = stk.pop() + num
                stk.append(int(num) * str(res))
        return ''.join(stk)
