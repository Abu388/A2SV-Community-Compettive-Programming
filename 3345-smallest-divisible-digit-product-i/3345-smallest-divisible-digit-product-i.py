class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod(res):
            l = 1
            for i in res:
                l *= i
            return l
        for i in range(n, n + 100):
            i = str(i)
            res = []
            for x in i:
                res.append(int(x))
            val = prod(res)
            if val % t == 0:
                return int(i)
            
                


        