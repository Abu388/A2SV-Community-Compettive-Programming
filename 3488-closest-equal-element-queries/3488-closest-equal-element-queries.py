from collections import defaultdict, Counter
from typing import List
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        
        # map value -> sorted list of indices
        hold = defaultdict(list)
        for i, num in enumerate(nums):
            hold[num].append(i)

        res = []

        for q in queries:
            val = nums[q]
            positions = hold[val]

            # if only one occurrence
            if len(positions) == 1:
                res.append(-1)
                continue

            # find position of q in sorted list
            idx = bisect.bisect_left(positions, q)

            # check neighbors in circular manner
            left = positions[idx - 1] if idx > 0 else positions[-1]
            right = positions[idx + 1] if idx < len(positions) - 1 else positions[0]

            # compute circular distances
            d1 = min(abs(q - left), n - abs(q - left))
            d2 = min(abs(q - right), n - abs(q - right))

            res.append(min(d1, d2))

        return res