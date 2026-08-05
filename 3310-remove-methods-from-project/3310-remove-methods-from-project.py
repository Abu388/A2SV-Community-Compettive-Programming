class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u , v in invocations:
            graph[u].append(v)
        
        visited = set()
        def dfs(k):
            if k in visited:
                return
            visited.add(k)
            for node in graph[k]:
                dfs(node)
        dfs(k)
        flag = True # all
        for u , v in invocations:
            if v in visited and u not in visited:
                flag = False
                break
            elif v not in visited and u in visited:
                flag = False
                break
        if not flag:
            res = []
            for i in range(0,n):
                res.append(i)
            return res
        else:
            res = []
            for i in range(0,n):
                if i not in visited:
                    res.append(i)
            return res


        