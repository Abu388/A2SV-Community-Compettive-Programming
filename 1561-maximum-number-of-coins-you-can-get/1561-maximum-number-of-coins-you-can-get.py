class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        if len(piles)==3:
            return piles[1]
        piles.sort()
        res=0
        n=len(piles)-1
        m=1
        count=len(piles)/3
        while count>0:
            res+=piles[n-m]
            print(piles[len(piles)-m])
            m+=2
            count-=1
        return res
        