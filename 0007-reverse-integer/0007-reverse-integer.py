class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 :
            return x
        if x<0:
            x= -x
            x=str(x)
            z=x[::-1]
            z=int(z)
            if z >2147483647:
                return 0
            else:
                z=-z
        elif x>0:
            x=str(x)
            z=x[::-1]
            z=int(z)
            if z> 2147483647:
                return 0
        return z