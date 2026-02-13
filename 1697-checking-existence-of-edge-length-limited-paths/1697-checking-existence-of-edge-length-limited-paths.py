class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        par = [i for i in range(n + 1)]
        def find(x):
            stk = []
            while x != par[x]:
                stk.append(x)
                x = par[x]
            while stk:
                par[stk.pop()] = x
            return x
        def union(u , v):
            x , y  = find(u) , find(v)
            if x == y:
                return 
            if x < y:
                par[y] = x
            else:
                par[x] = y
        edgeList = sorted(edgeList, key=lambda x: x[2])
        l = 0
        for q in queries:
            q.append(l)
            l += 1
        queries = sorted(queries , key=lambda x: x[2])
        res = [False] * len(queries)
        edgePointer = 0

        for p, q, limit, i in queries:       
            while edgePointer < len(edgeList) and edgeList[edgePointer][2] < limit:
                u, v, _ = edgeList[edgePointer]
                union(u, v)
                edgePointer += 1
            
            res[i] = (find(p) == find(q))
        
        return res



