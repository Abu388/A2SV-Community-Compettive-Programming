# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums 

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])  
        right = self.sortArray(nums[mid:])  
        i,j=0,0
        res=[]
        while i<len(left) and j < len(right):
            if left[i]>=right[j]:
                res.append(right[j])
                j+=1
            else:
                res.append(left[i])
                i+=1
        res.extend(left[i:])
        res.extend(right[j:])
        return res
            

        

    
       
        