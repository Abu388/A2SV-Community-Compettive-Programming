class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = {i:i for i in range(n)}
        indeg = {i:1 for i in range(n)}

        def find(x):
            while parent[x]!=x:
                x = parent[x]
            return x
        
        def join(x,y):
            parX = find(x)
            parY = find(y)

            if parX!=parY:
                if indeg[parX]<indeg[parY]:
                    parent[parY] = parX
                    indeg[parX]+= indeg[parY]
                else:
                    parent[parX] = parY
                    indeg[parY]+=indeg[parX]

        for i in range(n):
            for j in range(n):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    join(i,j)
        
        vis = set()
        ans = 0
        for i in range(n):
            par = find(i)
            if par not in vis:
                ans+= (indeg[par]-1)
                vis.add(par)

        return ans







