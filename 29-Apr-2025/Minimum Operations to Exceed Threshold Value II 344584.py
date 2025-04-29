# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        c = 0
        
        heapq.heapify(nums)

        while len(nums) > 1 and nums[0] < k:     
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums,(min(x, y) * 2 + max(x, y)))
            c += 1
        if nums[0] < k:
            return -1
        return c
