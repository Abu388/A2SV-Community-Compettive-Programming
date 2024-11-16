class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
#         if it grater if it less than and if it equal 
        costs.sort()
        count=0
        res=0
        for l,i in enumerate(costs):
            count+=i
            if count<coins:
                res+=1
            elif count==coins:
                return res+1
            
                
            
        return res
            