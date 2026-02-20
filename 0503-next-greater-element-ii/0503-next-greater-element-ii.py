class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = []
        res = [-1] * len(nums)
        for i in range(len(nums)):
            if not stk:
                stk.append((nums[i] , i))
            else:
                while stk and stk[-1][0] < nums[i]:
                    num , ind = stk.pop()
                    
                    res[ind] = nums[i]
                    
                stk.append((nums[i] , i))
        maxm = max(nums)
       
        while stk:
            num , ind = stk.pop()
            if num != maxm:
                for i , n in enumerate(nums):
                    if n > num:
                        res[ind] = n
                        break
        return res