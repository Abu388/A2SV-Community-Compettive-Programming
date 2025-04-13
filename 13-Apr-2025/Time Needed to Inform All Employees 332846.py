# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
       
        
        def dfs(node):
           
            if node not in graph:
                return 0
            res = 0
            for i in graph[node]:
                res = max(res,dfs(i))
            return res + informTime[node]

        graph = collections.defaultdict(list)
        for ind , val in enumerate(manager):
            graph[val].append(ind)
        
        return dfs(headID)