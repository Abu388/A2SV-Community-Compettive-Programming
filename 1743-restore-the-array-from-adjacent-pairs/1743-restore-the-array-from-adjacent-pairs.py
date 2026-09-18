class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        mp = defaultdict(list)
        val = defaultdict(int)
       
        for u, v in adjacentPairs:
            mp[u].append(v)
            mp[v].append(u)
            val[u] += 1
            val[v] += 1
        
        res = []
        visited = set()
        def dfs(node):
            res.append(node)
            visited.add(node)

            for n in mp[node]:
                if n not in visited:
                    dfs(n)
            

        for k in val.keys():
            if val[k] == 1:
                dfs(k)
                break
        
        return res



            

         
        
        

        