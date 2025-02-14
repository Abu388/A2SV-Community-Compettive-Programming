# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
       
        l = 0 
        r = 0 
        result = []  
        
        for idx, char in enumerate(s):
           
            r = max(r, last_occurrence[char])
            
            
            if idx == r:
                result.append(r - l + 1) 
                l = idx + 1  
        return result