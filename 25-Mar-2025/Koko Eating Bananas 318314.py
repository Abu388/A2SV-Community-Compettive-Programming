# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        def solu(mid):
            rsum=0
            for i in piles:
                rsum += ceil(i/mid)

                if rsum > h:
                    return False
            return True
            
        while l<=r:

            mid = (l+r)//2
            if solu(mid):
                r = mid -1
            else:
                l = mid + 1
        
        return l
        