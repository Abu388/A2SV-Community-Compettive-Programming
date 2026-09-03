class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd , eve = True, True
        d = float('inf')
        for i in nums1:
            if i % 2 == 0:
                eve = False
            else:
                d = min(i,d)
                odd = False
        if eve or odd:
            return True
       
        # even
        for i in range( len(nums1)):
            if nums1[i] % 2 == 0 and d >= nums1[i]:
                return False
                
              
            
        return True
                        



        