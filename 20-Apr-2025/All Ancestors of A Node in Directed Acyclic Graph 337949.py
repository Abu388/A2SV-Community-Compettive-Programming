# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        ancestors = [set() for _ in range(n)]
       
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
       
        queue = deque(i for i in range(n) if indegree[i] == 0)
        
        while queue:
            node = queue.popleft()
            
            for nei in graph[node]:
                
                ancestors[nei].update(ancestors[node])
                ancestors[nei].add(node)
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        
        return [sorted(list(ans)) for ans in ancestors]
        