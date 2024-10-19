class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arg2={}
        arg={}
        for c in s:
            if c in arg:
                arg[c]+=1
            else:
                arg[c]=1
        for j in t:
            if j in arg2:
                arg2[j]+=1


            else:
                arg2[j]=1
        if arg2==arg:
            return True
        return False
                