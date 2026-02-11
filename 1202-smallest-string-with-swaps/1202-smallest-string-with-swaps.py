class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        par = [i for i in range(n)]
        
        def find(x):
            stk = []
            while x != par[x]:
                stk.append(x)
                x = par[x]
            while stk:
                par[stk.pop()] = par[x]
            return x
        def union(u,v):
            x , y = find(u) , find(v)
            if x == y:
                return 
            if x > y:
                par[x] = y
            else:
                par[y] = x
            return
        for u , v in pairs:
            union(u,v)
        groups = defaultdict(list)
        res = list(s)

        for i in range(n):
            groups[find(i)].append(i)
        
        for indices in groups.values():
            chars = sorted(res[i] for i in indices)
            indices.sort()
            
            for i, c in zip(indices, chars):
                res[i] = c

        return "".join(res)
      
        