class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s=s1+' '+s2
        res=[]
        s=s.split()

        for i in set(s):
            if s.count(i)==1:
                res.append(i)
        return res