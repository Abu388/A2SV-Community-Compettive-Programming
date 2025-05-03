# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        res = []
        size = [1]*(n+1)
        parent = [i for i in range(n+1)]
        def find(x):
            stk  = []
            while parent[x] != x:
                stk.append(x)
                x = parent[x]
                
            while stk:
                parent[stk.pop()] = x
            return parent[x]

        def union(x,y):
            xu = find(x)
            yu = find(y)
            if xu == yu:
                res.append(x)
                res.append(y)

                return
            
            if size[xu] > size[yu]:
                xu , yu = yu , xu

            size[xu] += size[yu]
            parent[yu] = xu
    
        for x,y in  edges:                  
            union(x,y)
        return res