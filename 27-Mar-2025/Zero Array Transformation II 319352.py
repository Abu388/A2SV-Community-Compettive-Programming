# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:      
        def is_possible(mid):
            diff = [0] * (len(nums) + 1)
            for i in range(mid):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < len(nums):
                    diff[r + 1] -= val

            total_decrements = 0
            for i in range(len(nums)):
                total_decrements += diff[i]
                if nums[i] > total_decrements:
                    return False
            return True
        
        left = 0
        right = len(queries)

        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer if answer != -1 else -1