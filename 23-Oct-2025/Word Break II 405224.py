# Problem: Word Break II - https://leetcode.com/problems/word-break-ii/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        memo = defaultdict(tuple)
        def dp(i ,  val):
            if i == len(s):
                res.append(val)
                return 
            if (i,val) in memo:
                return memo[(i,val)]
           
            for w in wordDict:
                if s[i :i + len(w)] == w:
                    new_val = val + ' ' + w
                    memo[(i,val)] = dp(i + len(w), new_val)
                        
            
                    
        for w in wordDict:
            if s[ : len(w)] == w:
                dp(len(w) , w)
        return res

        