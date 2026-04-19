class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        #two nums nums1 is small and nums2 j is need to beiger enough 
        def bina(l,r,val):
            while l <= r:
                m = (l + r) // 2
                if nums1[m] > val:
                    l = m + 1
                else:
                    r = m - 1
            return l
        res = 0
        for j in range(len(nums2) - 1, -1 , -1):
            i = bina(0 , len(nums1) - 1, nums2[j])
            if i < len(nums1) and i <= j:
                res = max(j - i, res)
                
        return res