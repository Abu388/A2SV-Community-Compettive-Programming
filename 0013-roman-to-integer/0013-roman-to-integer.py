class Solution:
    def romanToInt(self, s: str) -> int:
        has={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9
        ,'XL':40,'XC':90,'CD':400,'CM':900}
        l=0
        res=0
        while l< len(s):
            if l<len(s)-1 and s[l:l+2] in has:
                res+=has[s[l:l+2]]
                l+=2
            else:
                res+=has[s[l]]
                l+=1
        return res


