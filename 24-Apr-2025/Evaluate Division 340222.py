# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ans = []
        visited = set()
        graph = defaultdict(dict)
        for i, value in enumerate(values):
            n, d = equations[i]
            graph[n][d] = value
            graph[d][n] = 1 / value

        def dfs(node , target , cur , visited):
            if node not in graph or target not in graph:
                return -1
            if node == target:
                return 1
            if target in graph[node]:
                return cur * graph[node][target]
            visited.add(node)
            for connection in graph[node]:
                if connection not in visited:
                    res = dfs(connection , target , cur * graph[node][connection] ,visited) 
                    if res != -1:
                        return res
            return -1
        for node , target in queries:
            value = dfs(node , target , 1, set())
            ans.append(value)
        return ans
        

        
        