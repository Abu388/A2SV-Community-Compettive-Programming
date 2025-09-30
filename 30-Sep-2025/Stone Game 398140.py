# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        #for the seck of the idea it is about the base case handling with two options okay
        @cache
        def dp( l , r , flag):
            alice = bob = 0
            if l > r:
                return 0
            
            if flag:
                alice = max(piles[l] + dp(l + 1 , r ,False), piles[r] + dp(l , r - 1 , False))
            else:
                bob = max(piles[l] + dp(l + 1 , r ,True), piles[r] + dp(l , r - 1 , True))
            
            return alice > bob

        return dp(0 , len(piles) - 1 , True)

            