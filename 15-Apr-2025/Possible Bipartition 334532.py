# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i,c in dislikes :
            graph[i].append(c)
            graph[c].append(i)
        color = [-1] * (n + 1)
        def dfs(node,c):
            color[node] = c
            for i in graph[node]:
                if color[i] == -1:
                    if not dfs(i,1-c):
                        return False
                elif color[i] == color[node]:
                    return False
            return True

        for i in range(len(graph)):
            if color[i] == -1:
                if not dfs(i,0):
                    return False
        return True
    
        
