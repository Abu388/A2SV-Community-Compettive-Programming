# Problem: Peak Index in a Mountain Array - https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l , r = 0 , len(arr) - 1
        
        while l <= r:
            m = (l + r) // 2

            if (m + 1) < n and arr[m] <= arr[m + 1]: # the odd part
                l = m + 1
            elif (m - 1) > -1 and arr[m] <= arr[m - 1]:
                r = m - 1
            else:
                return m
        