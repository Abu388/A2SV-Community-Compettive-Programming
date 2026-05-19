class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
   
        num = sorted(set(nums1))
        nums5 = set(nums2)
        for n in num:
            if n in nums5:
                return n
        return -1
        