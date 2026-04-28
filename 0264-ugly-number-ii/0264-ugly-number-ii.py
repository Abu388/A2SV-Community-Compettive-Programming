class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visited = set()
        factor = [ 2, 3, 5] 
        for i in range(n):
            num = heapq.heappop(heap)
            if i == n - 1:
                return num
            
            for f in factor:
                if f * num not in visited:
                    visited.add(f * num)
                    heapq.heappush(heap, f * num)
            