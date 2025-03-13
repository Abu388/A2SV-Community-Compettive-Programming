# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 1 :
            return True
        if n <= 0:
            return False
        flag=False
        x=32
        def sol(x):
            nonlocal n,flag
            if x == 1:
                return 2
            
            prev=sol(x-1)
            curRes=2*prev
            if curRes==n or prev==n:
                flag=True
            
            return curRes
        sol(x)
        return flag

    #     if res == n:
    #         return True
    #     if res > n:
    #         return False

    # return False
            
        