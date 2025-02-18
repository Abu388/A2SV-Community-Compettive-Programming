# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[]
        sufi=[]
        arr=[]
        total=1
        for i in nums:
            total*=i
            pref.append(total)
        total=1
        
        for j in nums[::-1]:
            total*=j
            sufi.append(total)
        sufi=sufi[::-1]

        arr.append(sufi[1])
        for k in range(1,len(nums)-1):
            arr.append(pref[k-1]*sufi[k+1])
        arr.append(pref[len(nums)-2])
        return arr

          
        
      
        
      

