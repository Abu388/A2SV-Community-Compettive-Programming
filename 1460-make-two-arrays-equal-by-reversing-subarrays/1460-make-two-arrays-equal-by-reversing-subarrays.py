class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        for n,i in enumerate(arr):
            if target[n]!=i:
                return False
        return True 
        
        