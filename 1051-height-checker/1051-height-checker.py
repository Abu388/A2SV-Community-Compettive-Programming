class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        arr=heights.copy()
        arr.sort()
        count=0
        
        for l, i in enumerate(heights):
            if arr[l]!= i:
                count+=1
        return count
                
        