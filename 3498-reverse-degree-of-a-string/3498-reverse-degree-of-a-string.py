class Solution:
    def reverseDegree(self, s: str) -> int:
        alp = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
        res = 0
        for i in range(len(s)):
            res += (i + 1) * (ord(alp[ ord(s[i] ) - 97]) - 96)
        return res
            

        
