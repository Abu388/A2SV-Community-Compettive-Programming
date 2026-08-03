class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        @cache
        def dp(i):
          
            if i == n:
                return 0
            
            max_diff = float('-inf')
            current_take = 0
            
            for k in range(1, 4):
                if i + k - 1 < n:
                 
                    current_take += stoneValue[i + k - 1]
                    

                    max_diff = max(max_diff, current_take - dp(i + k))
                    
            return max_diff
        

        alice_advantage = dp(0)
        
        if alice_advantage > 0:
            return "Alice"
        elif alice_advantage < 0:
            return "Bob"
        else:
            return "Tie"