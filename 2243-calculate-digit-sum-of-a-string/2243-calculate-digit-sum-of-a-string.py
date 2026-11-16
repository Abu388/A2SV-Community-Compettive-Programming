class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            first = ''
            res = []
            for i in range(len(s)):
                if i != 0 and  i % k == 0:
                    first += str(sum(res))
                    
                    res = []
                res.append(int(s[i])) 
            first += str(sum(res))
            s = first 
       
        return s
        
