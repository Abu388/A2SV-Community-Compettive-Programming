# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window=0
        max_val=float('-inf')
        window=sum(nums[:k])
        max_val=max(window,max_val)
        ind=0
        for i in range(k,len(nums)):
            window-=nums[ind]
            window+=nums[i]
            max_val=max(window,max_val)
            ind+=1
            
        return max_val/k






# if i <k:
            #     window+=nums[i]
            
            # average=window//k
        
            # max_val=max(max_val,average)

        
        
        
            
            
            
        
        