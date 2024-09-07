from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        y=""
        for i in range(len(indices)):
            y+=s[indices.index(i)]
            
        return y
        
        
        
                
        
            

        
    
