class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights),sum(weights)

        def solu(mid):
            rsum = 0
            day = 1
            for weight in weights:
                rsum += weight
                if rsum > mid:
                    day += 1
                    rsum = weight
            if day > days:
                return False
            return True

        while l<=r:
            mid = (l+r)//2
            if solu(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
