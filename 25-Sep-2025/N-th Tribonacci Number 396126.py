# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1
        if n == 0:
            return 0
        if n < 3:
            return 1

        def solu(i , val):
            nonlocal t0 , t1 ,t2
            t0 , t1 ,t2 = t1 , t2 ,val

            
            if i < n - 3:
                solu(i + 1 ,t0 + t1 + t2 )
            return t2

        return solu(0, t0 + t1 + t2)
            