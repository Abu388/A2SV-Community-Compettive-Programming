# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        
        def recurtion(s):
            val = ''.join(str(1-int(i)) for i in s)
            return s + '1' + val[::-1]
        for _ in range(n):
            s = recurtion(s)
        return s[k-1]
            
        


       
       


       
