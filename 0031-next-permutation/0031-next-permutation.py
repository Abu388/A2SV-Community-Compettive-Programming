class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def check(i):            
            while i > 0:
                if nums[i - 1] < nums[i]:
                    return i - 1
                i -= 1
            return -1
        t = check(len(nums) - 1)
        if t == -1:
            nums.sort()
            return  

        minm = float('inf')
        hold = -1
        for i in range(len(nums) - 1, t, -1):
            if nums[i] > nums[t]:
                nums[i], nums[t] = nums[t], nums[i]
                break
        nums[t + 1:] = reversed(nums[t + 1:])

        

        


        

        

        