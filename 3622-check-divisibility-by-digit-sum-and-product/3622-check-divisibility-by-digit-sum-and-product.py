class Solution:
    def checkDivisibility(self, n: int) -> bool:
        v = str(n)
        s = 0
        p = 1
        for i in v:
            s += int(i)
            p *= int(i)
        
        if n % (s + p) == 0:
            return True
        return False
         
        
        