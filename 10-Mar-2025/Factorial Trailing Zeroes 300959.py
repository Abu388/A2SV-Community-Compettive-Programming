# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

from collections import Counter
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0

        
        def res(n):
            if n==0 or n==1:
                return 1
            return n*res(n-1)  
        f=res(n)
        while f%10==0:
            count+=1
            f=f//10
        return count
        
     
      