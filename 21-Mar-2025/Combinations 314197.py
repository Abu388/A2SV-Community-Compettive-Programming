# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def solu(i,arr):
            if len(arr) == k:
                res.append(arr.copy())
                return            
            
            for j in range(i,n+1):
                arr.append(j)
                
                solu(j + 1, arr)
               
                arr.pop()
                
                

        solu(1,[])
        return res
    


            


        
        