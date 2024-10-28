class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()
        l=len(capacity)-1
        count=0
        res=0
        while l>=0:
            count+=1
            res+=capacity[l]
            if sum(apple)<=res:
                return count
            
            l-=1
        return count
        
            