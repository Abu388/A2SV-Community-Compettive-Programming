# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

from collections import defaultdict
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total=0
        has=[]
        for a,b in costs:
            has.append((a,b,a-b))
        
        has.sort(key=lambda x:x[2])
        one=len(costs)//2
    
        for a,b,c in has:
            if one>0:
                total+=a
            else:
                total+=b
            one-=1
         

        return total

        



        