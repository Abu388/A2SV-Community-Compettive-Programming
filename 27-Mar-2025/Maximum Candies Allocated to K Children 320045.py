# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def valid(mid):
            total = 0
            for i in range(len(candies)):
                total += (candies[i]//mid)
            return total >= k
       
        ans = 0
        l,r = 1,max(candies)
        while l<= r:
            mid = (l+r)//2
            if valid(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid -1
        return ans

