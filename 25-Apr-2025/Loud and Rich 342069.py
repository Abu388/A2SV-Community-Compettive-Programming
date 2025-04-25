# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        
        ind = [-1]*len(quiet)
        
       
        
        
        for a , b in richer:
            graph[b].append(a)
            
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            new_val = node

            for chiled in graph[node]:
                final = dfs(chiled)
                if quiet[new_val] > quiet[final]:
                    new_val = final
            visited[node] = new_val
            return new_val
        for key in range(len(quiet)):
            val = dfs(key)
            ind[key] = val 
        
        return ind