class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10 :
            return False

        r = 10
        while n > 0:
            n -= r
            r -= 1
            if n == 0:
                if r % 2 == 0:
                    return False
                return  True  
   
        if r % 2 == 0:
            return True
        return False 


        