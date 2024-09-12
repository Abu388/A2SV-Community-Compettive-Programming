class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed=set(allowed)
        res=len(words)
        for c in words:
            for i in c:
                if i not in allowed:
                    res-=1
                    break
        return res
                
        