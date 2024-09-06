class Solution:
    def firstUniqChar(self, s: str) -> int:
        store = {}

    
        for i in s:
            if i not in store:
                store[i] = 1
            else:
                store[i] += 1


        for key, value in store.items():
            if value == 1:
                for n, j in enumerate(s):
                    if key == j:
                        return n  

        return -1




       
            
        
                    
                    
        
            



        