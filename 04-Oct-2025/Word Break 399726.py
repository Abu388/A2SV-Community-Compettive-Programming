# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i):   
            if i == len(s) :
                return True
            
            for word in wordDict:
                nr = len(word) - 1
                if i + nr < len(s) and s[i: i + nr + 1] == word:
                    if dp(i + nr + 1):
                        return True
            return False

            

        return dp(0)