# Problem: Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        memo = defaultdict(int)
        def dp(i ,buy):
            if i == len(prices):
                print(i)
                return 0
            if (i,buy ) in memo:
                return memo[(i,buy)]

            if buy:#it is time to buy
                res = max(-prices[i] + dp(i + 1 ,False) , dp(i + 1, True))
                memo[(i,buy)] = res
                return res
            else:
                res = max(prices[i] + dp(i + 1, True) , dp(i + 1, False))
                memo[(i,buy)] = res
                return res 
        
        return dp(0,True)

