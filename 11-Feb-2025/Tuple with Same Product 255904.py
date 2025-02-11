# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

from collections import Counter
class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product=[]
        total=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                
                product.append(nums[i]*nums[j])
        
        dictionary={}
        for k in product:
            dictionary[k]=dictionary.get(k,0)+1

        for val in dictionary.values():
            if val>1:
                n=val-1
                c=n*(n+1)//2
                total+=c*8
        return total
            