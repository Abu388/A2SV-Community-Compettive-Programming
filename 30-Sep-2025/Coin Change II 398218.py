# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i , val):
            nonlocal amount
            res = 0
            if val == amount:
                return 1
            if val > amount or i == len(coins):
                return 0
            if (i,val) in memo:
                return memo[(i,val)]
            
            res = dp(i, val + coins[i]) + dp(i + 1, val)
            memo[(i,val)] = res
            return res
        return dp(0 , 0)