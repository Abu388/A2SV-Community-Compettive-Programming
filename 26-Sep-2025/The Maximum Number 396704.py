# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        n = [i for i in s]
        n.sort()
        if len(n) < 3:
            return max(n)
        
        print(n)
        return n[len(n) - 3 ]
        