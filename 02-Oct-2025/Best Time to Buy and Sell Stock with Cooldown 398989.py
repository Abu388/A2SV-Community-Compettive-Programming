# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i ,val):
            buy = sell  = 0
            if  i >= len(prices) :
                return 0
             
            if val :# it is time to buy
                buy =  max(-prices[i] + dp(i + 1, False) ,dp(i + 1, True))
            else :# time to buy 
                sell = max(prices[i] + dp(i + 2, True) ,dp(i + 1, False))

            return buy + sell
        
        return dp(0,True)

                

        