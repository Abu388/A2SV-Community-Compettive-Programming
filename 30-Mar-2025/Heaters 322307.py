# Problem: Heaters - https://leetcode.com/problems/heaters/

import bisect
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        final = 0
        for i in houses:
            ind = bisect.bisect_left(heaters,i)
            left = heaters[ind-1] if ind > 0 else float('inf')
            right = heaters[ind] if ind < len(heaters) else float('inf')


            cur = min(abs(i-left),abs(i-right))

            final = max(final,cur)
        return final
            