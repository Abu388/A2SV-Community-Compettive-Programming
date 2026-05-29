class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float('inf')
        for j in range(len(nums)):
            n = str(nums[j])
            c = 0
            for i in n:
                c += int(i)
            res = min(res, c)
        return res
        
        


            
