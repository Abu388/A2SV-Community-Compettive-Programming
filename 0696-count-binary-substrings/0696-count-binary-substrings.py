class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prv = res = 0
        cur = 1
        for  i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(prv,cur)
                prv = cur
                cur = 1
        res += min(prv,cur)
        return res