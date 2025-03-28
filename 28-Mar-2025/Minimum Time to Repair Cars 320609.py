# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def valid(mid):
            total = 0
            for i in ranks:
                i = mid/i
                total += math.floor(pow(i,0.5))

            if total >= cars:
                return True
            return False





        l = 1
        r = max(ranks)*(cars**2)
        while l <= r:
            mid = (l+r)//2
            if valid(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l