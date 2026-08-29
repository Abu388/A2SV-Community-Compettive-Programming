class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=0
        
        for i in range(len(s)):
            if s[i] != ' ':
                l=i
        r=l
        while s[l] != " " and l>=0:
            l-=1
        
        return r-l