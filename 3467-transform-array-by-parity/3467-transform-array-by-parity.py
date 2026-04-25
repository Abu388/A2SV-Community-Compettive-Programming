class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        res1 = res0 = 0
        for n in nums:
            if n % 2 :
                res1 += 1
            else:
                res0 += 1
        
        return ([0] * res0) + ([1] * res1) 