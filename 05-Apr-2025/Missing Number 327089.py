# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total,n = 0,0
        
        for i in range(len(nums)+1):
            total += n
            n +=1
        
        return total-sum(nums)
        

             
        
           
        
        