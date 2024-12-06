class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Sort nums to build the smallest possible subsequence
        nums.sort()
        
        # Compute prefix sums
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
        
        # For each query, find the maximum subsequence size
        res = []
        for query in queries:
            # Find the largest index where the sum is <= query
            l, r = 0, len(prefix_sums) - 1
            while l <= r:
                mid = (l + r) // 2
                if prefix_sums[mid] <= query:
                    l = mid + 1
                else:
                    r = mid - 1
            res.append(r)
        
        return res

                
        
            
            