class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        mp = {}
        for n in range(len(colors)):
            if colors[n] not in mp:
                mp[colors[n]] = n
        res = 0
        for i in mp.values():
            for j in range(len(colors) - 1, - 1, -1):
                if colors[j] != colors[i]:
                    res = max(res,  abs(j - i))
                    break
        return res