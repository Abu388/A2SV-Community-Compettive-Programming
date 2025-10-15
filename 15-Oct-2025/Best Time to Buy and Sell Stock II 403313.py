# Problem: Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i , buy):
            res = val = 0

            if i == len(prices):
                return 0
            if (i , buy) in memo:
                return memo[(i,buy)]
            

            if not buy:
                res = max(-prices[i] + dp(i + 1, True) , dp(i + 1 , False))
            else:
                val = max(prices[i] + dp(i + 1, False) , dp(i + 1 , True))
            memo[(i,buy)] = max(res , val)

            return memo[(i,buy)]

            
        
        return dp(0 , False)