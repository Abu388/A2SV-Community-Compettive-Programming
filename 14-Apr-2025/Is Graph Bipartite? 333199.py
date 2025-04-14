# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        def dfs(node,c):
            color[node] = c
            for chiled in graph[node]:
                if color[chiled] == -1:
                    if not dfs(chiled , 1-c):
                        return False
                elif color[chiled] == color[node]:
                    return False
            return True

        for i in range(n):
            if color[i] == -1:
                if not dfs(i,0):
                    return False
        return True
