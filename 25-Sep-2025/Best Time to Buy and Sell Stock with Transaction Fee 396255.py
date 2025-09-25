# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = defaultdict(int)
        def dp(i , buy):

            if i == len(prices):
                return 0
            if (i,buy) in memo:
                return memo[(i,buy)]
            if buy:
                res = max(- prices[i]+ dp(i + 1, False) , dp(i + 1, True))
                memo[(i,buy)] = res
                return res
            else:
                res = max(prices[i] + dp(i + 1, True) - fee , dp(i + 1, False))
                memo[(i,buy)] = res
                return res


        return dp(0,True)

        #use and not use in maximum
        