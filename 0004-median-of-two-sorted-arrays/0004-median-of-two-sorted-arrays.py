class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        l , r = 0 ,0 
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                res.append(nums1[l])
                l += 1
            else:
                res.append(nums2[r])
                r += 1
        if r == len(nums2):
            res = res + nums1[l: ]
        if l == len(nums1):
            res = res + nums2[r: ]
        

        if len(res) % 2:
            return res[len(res) // 2] 
        else:
            up = res[len(res) // 2] 
            down = res[(len(res) // 2) - 1]
            return (down + up) / 2
            
