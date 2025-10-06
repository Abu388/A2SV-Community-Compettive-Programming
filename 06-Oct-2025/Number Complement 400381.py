# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        n = list(i for i in bin(num))
        res = ['0'] * len(n)
        
        for i in range(len(n) - 1, -1, -1):
            
            if n[i] == 'b':
                break
            if n[i] == '0':
                res[i] = '1'
        
        return int(''.join(res) , 2)