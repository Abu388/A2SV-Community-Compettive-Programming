# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = []
        for i in range(len(costs)):
            sub = costs[i][1] - costs[i][0]
            res.append((sub , i))
        res.sort()
        l = 0
        summ = 0
        for i in range(len(res)//2):
            val , ind = res[i]
            summ += costs[ind][1]
            
        for i in range(len(res)//2, len(res)):
            val , ind = res[i]
            summ += costs[ind][0]

        return summ 
        
        

        



        