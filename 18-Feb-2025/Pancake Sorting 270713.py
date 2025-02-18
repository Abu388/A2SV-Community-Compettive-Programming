# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        
        def flip(k):
            arr[:k] = arr[:k][::-1]
        
        for target in range(len(arr), 0, -1):
            idx = arr.index(target)
            
            if idx == target - 1:
                continue  # Already in place
            
            if idx != 0:
                flip(idx + 1)
                res.append(idx + 1)
            
            flip(target)
            res.append(target)
        
        return res

        