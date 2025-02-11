# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        total=0
        n=len(piles)
        pick_val=n//3
        while pick_val>0:
            n=n-2
            total+=piles[n]
            pick_val-=1
        return total
        


        