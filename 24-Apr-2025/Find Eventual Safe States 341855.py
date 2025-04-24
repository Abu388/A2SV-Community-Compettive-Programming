# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        indegree = [0] * n
        res = []

        
        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u)
            indegree[u] = len(graph[u])
        
        q = deque(i for i in range(len(indegree)) if indegree[i] == 0)
        print(q)
        while q:
            node = q.popleft()
            for chiled in reverse_graph[node]:
                indegree[chiled] -= 1
                if indegree[chiled] == 0:
                    q.append(chiled)
        for i in range(len(indegree)):
            if indegree[i] == 0:
                res.append(i)
        return res
        

        