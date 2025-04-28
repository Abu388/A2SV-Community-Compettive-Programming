# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        val = []
        for i in piles:
            val.append(-i)
        heapq.heapify(val)

        for _ in range(k):       
            c = -heapq.heappop(val)
            opp = c - c//2
            heapq.heappush(val,-opp)
        return -sum(val)