class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        arr = []
        res = []
        arr.append(nums[0])
        res.append(nums[1])
        a = r = 0
        for i in range(2, len(nums)):
            if arr[len(arr) - 1] > res[len(res) - 1]:
                arr.append(nums[i])
            else: res.append(nums[i])
        return arr+res


        