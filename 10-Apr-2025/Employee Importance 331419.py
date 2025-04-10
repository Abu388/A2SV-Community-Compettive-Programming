# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        

        visited = set()
        graph = {}
        has = defaultdict(int)
        total = 0
        
        for i in range(len(employees)):
            has[employees[i].id] += employees[i].importance
            graph[employees[i].id]=employees[i].subordinates
        
        def dfs(id):
            nonlocal total
            if id not in visited:
                total += has[id]
            for g in graph[id]:
                if g not in visited:
                    total += has[g]
                    visited.add(g)                    
                    dfs(g)
    
        dfs(id)
        return total













