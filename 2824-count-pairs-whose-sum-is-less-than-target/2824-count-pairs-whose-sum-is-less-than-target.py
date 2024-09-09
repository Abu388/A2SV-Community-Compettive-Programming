class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count=0
        l=0
        while l<len(nums)-1:
            for i in range(l+1,len(nums)):
                if nums[l]+nums[i]<target:
                    count+=1
            l+=1
        return count
    
        