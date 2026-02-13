class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        par = [ i for i in range( n + 1) ] 
        def find(x):
            stk = []
            while x != par[x]:
                stk.append(x)
                x = par[x]
            while stk:
                par[stk.pop()] = x
            return x
        def union(u, v):
            x , y = find(u) , find(v)
            if x == y:
                return
            if x < y:
                par[y] = x
            else:
                par[x] = y
            return
        for u , v , dis in roads:
            union(u,v)
        res = float('inf')
        for u , v , dis in roads:
            if find(u) == 1 and find(v) == 1:
                res = min(res, dis)
        return res
