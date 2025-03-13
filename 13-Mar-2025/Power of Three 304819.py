# Problem: Power of Three - https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n < 1 :
            return False
        if n == 1:
            return True
        flag=False
        x=32
        def solu(x):
            nonlocal n,flag
            if x == 1:
                return 3
            
                        
            res=solu(x-1)
            print(res)
            if res == n:
                flag=True
            res=3*res

         
            return res
        solu(x)

        return flag
        