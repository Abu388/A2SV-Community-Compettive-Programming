# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in matrix:
            for val in row:
                heapq.heappush(heap,val)
        
        
        for _ in range(k-1):
            heapq.heappop(heap)
            
        return heapq.heappop(heap)