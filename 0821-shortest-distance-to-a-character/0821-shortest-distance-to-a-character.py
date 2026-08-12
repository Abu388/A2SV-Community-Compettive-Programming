class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        mp = set()
        for i in range(len(s)):
            if s[i] == c:
               mp.add(i)
        res = []
        for i in range(len(s)):
            x = float('inf')
            for j in mp:
                x = min(x, abs(i - j))
            res.append(x)
        return res
            
            