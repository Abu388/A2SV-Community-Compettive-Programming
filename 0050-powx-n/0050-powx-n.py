class Solution:
    def myPow(self, x: float, n: int) -> float:
        #if n is negative
        #if n is odd
        #if x is zero
        if x == 0:
            return 0
        if  n == 0:
            return 1
        
        def power(x,n):

            if n == 1 :
                return x

            res=power(x,n//2)

            res*=res
            if n % 2 != 0:
                res*=x

            return res
        final=power(x,abs(n))
        return final if n > 0 else 1/final

       