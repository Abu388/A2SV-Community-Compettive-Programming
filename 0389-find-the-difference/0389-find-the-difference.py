class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        has = {}
        for i in t:
            if i not in has:
                has[i] = 1
            else:
                has[i] += 1

        for i in s:
            if i in has:
                has[i] -= 1
            else:
                has[i] = -1 

        for key, value in has.items():
            if value != 0:
                return key  

                