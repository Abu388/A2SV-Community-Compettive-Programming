# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        degree = {}
        leaves = deque()
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        for k ,v in graph.items():
            if len(v) == 1:
                leaves.append(k)
            degree[k] = len(v)
        length = n
        while length > 2: 
            length -= len(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                for ng in graph[node]:
                    degree[ng] -= 1
                    if degree[ng] == 1:
                        leaves.append(ng)
        return list(leaves)

        
