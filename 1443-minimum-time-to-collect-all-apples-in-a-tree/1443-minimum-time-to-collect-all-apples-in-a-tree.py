class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)

        for u , v in edges:
            graph[u].append(v )
            graph[v].append(u)
 
        def dfs(node , par):
            time = 0
            for nig in graph[node]:
                if nig == par:
                    continue
                nex = dfs(nig , node)
                if nex > 0 or hasApple[nig]:
                    time += nex + 2
            return time
        
        return dfs(0, -1)

