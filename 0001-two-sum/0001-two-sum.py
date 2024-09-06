class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        arr=[]
        for l in range(len(nums)-1):
            for r in range(l+1,len(nums)):
                if nums[l]+nums[r] != target:
                    r += 1
                else:
                    arr.append(l)
                    arr.append(r)
            
        return arr
        
        