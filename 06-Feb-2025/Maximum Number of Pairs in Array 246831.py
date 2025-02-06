# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size=0
        two=0
        has={}
        for i in nums:
            has[i]=has.get(i,0)+1
        for keys,value in has.items():
            if value %2 ==0:
                size+=value//2

            else:
                
                value-=1 
                size+=value//2
                two+=1


        return [size,two]
