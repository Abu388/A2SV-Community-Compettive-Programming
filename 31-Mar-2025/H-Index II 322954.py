# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def valid(mid):
            return citations[mid] >= len(citations) - mid
        l,r =  0,len(citations )-1
        while l<=r:
            mid = (l+r)//2
            if valid(mid):
                r = mid - 1
            else:
                l = mid + 1
        return len(citations ) - l
