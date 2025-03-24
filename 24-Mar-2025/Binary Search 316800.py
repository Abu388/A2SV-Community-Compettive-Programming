# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = (r+l)//2
        while l<=r:
            if nums[mid] < target:
                l = mid +1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
            mid = (r+l)//2
        return -1

    