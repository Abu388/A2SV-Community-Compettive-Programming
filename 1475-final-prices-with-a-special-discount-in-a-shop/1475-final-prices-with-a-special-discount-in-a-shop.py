class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        nums=prices
        arr=nums
        if len(nums)==1:
            return nums
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>=nums[j]:
                    arr[i]=(nums[i]-nums[j])
                    break
        return arr
                    
                
            
        