from collections import defaultdict

class Solution:
    def validArrangement(self, pairs):
        # adjacency list
        graph = defaultdict(list)

        # degree counts
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        # Build graph and count degrees
        for u, v in pairs:
            graph[u].append(v)
            outdegree[u] += 1
            indegree[v] += 1

        # Find the starting node
        #
        # Eulerian Path rule:
        # start node has:
        # outdegree = indegree + 1
        #
        # If no such node exists, we can start from
        # any node with outgoing edges.
        start = pairs[0][0]

        for node in outdegree:
            if outdegree[node] - indegree[node] == 1:
                start = node
                break

        path = []

        def dfs(node):
            # Keep consuming edges until none remain
            while graph[node]:
                nxt = graph[node].pop()
                dfs(nxt)

            # Add node AFTER all outgoing edges are used
            # (postorder traversal)
            path.append(node)

        dfs(start)

        # Hierholzer builds the path backwards
        path.reverse()

        # Convert node path into edge path
        answer = []

        for i in range(len(path) - 1):
            answer.append([path[i], path[i + 1]])

        return answer