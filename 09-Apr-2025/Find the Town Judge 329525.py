# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

from collections import defaultdict,Counter
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if trust == []:
            if n == 1:
                return 1
            
        graph = defaultdict(list)
        n = n-1
        total_j = set()
        visited = set()
        for p, j in trust:
            graph[p].append(j)
            total_j.add(j)        
        values = [i  for v in graph.values() for i in v]
        for k in graph.keys():
            visited.add(k)       
       
        for i in total_j:
            found = values.count(i)
            if i not in visited and found == n:
                return i
        return -1
 
