# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

from collections import defaultdict
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        has=defaultdict(int)
        has2=defaultdict(int)
        stk=[]
        for ind,value in enumerate(arr):
            while stk and stk[-1][0]>value:
            
                v,i=stk.pop()
                has[i]=ind-i
                
                
            stk.append((value,ind)) 

        while stk:
            v,i=stk.pop()   
            has[i]=len(arr)-i         
        stk=[]
        
        for ind in range(len(arr)-1,-1,-1):
            while stk and stk[-1][0]>=arr[ind]:            
                v, i =stk.pop()
                has2[i]=i-ind
                
            
            stk.append((arr[ind],ind)) 
           
            

        while stk:
            v,i=stk.pop() 
            has2[i]=i+1
                      
            
        result = sum(arr[i] * has[i] * has2[i] for i in range(len(arr))) % (10**9 + 7)
        return result









