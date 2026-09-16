import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        total_points = n + k - 1
        endpoints_needed = 2 * k
        
        return math.comb(total_points, endpoints_needed) % MOD