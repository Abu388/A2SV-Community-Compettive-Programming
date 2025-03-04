# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        has={1:-1, 0:0}
        res=[0]*len(s)
        for i in range(len(s)):
            has[int(s[i])]+=1
        one=has[1]
        zero=has[0]
        for i in range(one):
            res[i]=1
        res[len(s)-1]=1
        return ''.join(map(str,res))

        
        
