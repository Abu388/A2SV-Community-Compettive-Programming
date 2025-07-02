# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count1 = bin(num2).count('1')  
        result = 0
        
        for i in reversed(range(32)):
            if num1 & (1 << i) and count1 > 0:
                result |= (1 << i)
                count1 -= 1
        for i in range(32):
            if not (result & (1 << i)) and count1 > 0:
                result |= (1 << i)
                count1 -= 1
        
        return result
