# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r=0,len(s1)-1
        if len(s1)>len(s2):
            return False
        checker=[i for i in s2[l:len(s1)]]
        if Counter(checker) == Counter(s1):
            return True

        while r<len(s2)-1:
            checker.pop(0)
            r+=1
            checker.append(s2[r])

            if Counter(checker) == Counter(s1):
                return True
          
        return False
        
                
                
        
       
        
                   
                        
            
                                
                
                    
                    
        