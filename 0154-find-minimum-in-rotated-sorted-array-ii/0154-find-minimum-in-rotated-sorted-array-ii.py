class Solution:
    def findMin(self, nums: List[int]) -> int:
        val = set()
        res = []
        for i in nums:
            if i not in val:
                val.add(i)
                res.append(i)
        def valid(r,mid):
            return nums[r] > nums[mid]
        l , r = 0 , len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if valid(r, mid):
                r = mid
            else:
                l = mid + 1
        return nums[r]


        