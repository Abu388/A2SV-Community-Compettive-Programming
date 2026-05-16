class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        mp = defaultdict(int)

        for i in stones:
            mp[i] += 1
        res = 0
        val = set()
        for i in jewels:
            if i not in val:
                res += mp[i]
        return res

