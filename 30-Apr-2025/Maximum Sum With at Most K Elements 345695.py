# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        value = []
        res = 0
        heapify(value)
        for l in range(len(limits)):
            m = []
            heapify(m)
            for j in grid[l]:
                heappush(m,-j)            
            for _ in range(limits[l]):
                c = heappop(m)
                heappush(value,c)

        for _ in range(k):
            res += heappop(value)
        return -res

                
        
