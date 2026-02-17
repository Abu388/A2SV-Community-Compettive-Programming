class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0: - 1}
        tot = 0
        for i , n in enumerate(nums):
            tot += n
            r = tot % k
            if r not in mp:
                mp[r] = i
            elif i - mp[r] > 1:
                return True
        return False
