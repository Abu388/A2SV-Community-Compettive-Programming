# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:   
        memo = defaultdict(int)  
        flag = False
        if amount == 0:
            return 0
        
        
        def solu(val):
            nonlocal flag
            res = count = float('inf')
        
            
            if val == 0:
                flag = True
                return 0 
            if val in memo:
                return memo[val]
            for num in range(len(coins)):
                if val - coins[num]  > -1:
                    count = 1 + solu(val - coins[num])
                    res = min(res,count)
                    memo[val] = res
            
            return res

        res = solu(amount)
        if flag:
            return res
        else:
            return -1

        
