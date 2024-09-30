class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        
        r=nums[len(nums)-1]*nums[len(nums)-2]
        l=nums[0]*nums[1]
        return r-l