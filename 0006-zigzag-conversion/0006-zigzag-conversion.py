class Solution:
    def convert(self, s: str, numRows: int) -> str:
        m = [[] for _ in range(numRows)]
        res = ''
        i = 0
        while i < len(s):

            l = 0
            while i < len(s) and l < len(m):
                m[l].append(s[i])
                l += 1
                i += 1

            d = len(m) - 2
            while i < len(s) and 0 < d:
                m[d].append(s[i])
                d -= 1
                i += 1
        
        for val in m:
            res += ''.join(val)
        return res
            
            
        

            

             