class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res = float('inf')
        for i in range(len(nums)):
            v = 0
            t = []
            for j in range(i, i + r ):
                if j >= len(nums):
                    break

                v += nums[j]
                t.append(nums[i])
                if v > 0 and len(t) >= l:
                    
                    res = min(res, v)
        if res == float('inf'):
            return -1
        return res
                

        