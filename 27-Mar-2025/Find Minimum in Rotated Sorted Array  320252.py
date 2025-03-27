# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        def valid(r,mid):
            return nums[r] >= nums[mid]
        
        l = 0
        r = len(nums)-1
        ans = float('inf')
        while l <= r:
            mid = (l+r)//2    
            ans=min(ans,nums[mid],nums[l],nums[r])        
            if valid(r,mid): 
                r = mid - 1         
                
            else:
                l = mid + 1
        
        return ans



  