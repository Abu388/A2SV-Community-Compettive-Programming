class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        mp = {}
        res = float('inf')

        for i, n in enumerate(nums):
            if n in mp:
                res = min(res, i - mp[n])

            reversed_n = int(str(n)[::-1])
            mp[reversed_n] = i

        return res if res != float('inf') else -1