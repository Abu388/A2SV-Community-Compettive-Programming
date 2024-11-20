class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l=0
        
        res=[]
        count=float("-inf")
        while l< len(s):
            
            if s[l] not in res:
                res.append(s[l])
                count=max(count,len(res))
                l+=1
            else:
                res.pop(0)
        return count
            
        