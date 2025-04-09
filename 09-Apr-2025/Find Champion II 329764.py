# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

from collections import defaultdict
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        champion = set()
        val = set()
        res = []
        for c , l in edges:
            graph[c].append(l)
            champion.add(c)
            val.add(l)
        if  edges == []:
            if n == 1:
                return 0
            else:
                return -1
        l = 0
        while l < n:
            if l in champion or l in val:
                l+=1
            else:
                return -1
       

        
        
        weaker  = {v for weaker  in graph.values() for v in weaker  }
      
       
        for i in champion:
            if i not in weaker :
                res.append(i)
        if len(res) >1:
            return -1
        else:
            return res[0]
                
        return -1
       
