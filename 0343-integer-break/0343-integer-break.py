class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        mp = {1 : 1}
        def dp(num):
            if num in mp:
                return mp[num]
            mp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dp(i) * dp(num - i)
                mp[num] = max(val, mp[num])
            return mp[num]

        return dp(n)
