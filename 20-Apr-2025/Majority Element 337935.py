# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        visited = set()
        n = len(nums) / 2
        for i in nums:
            if i not in visited:
                visited.add(i)
                c = nums.count(i)
                if c >= n:
                    return i
            
            
        