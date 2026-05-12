class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n - 1:
            return -1
        self.parent = {i: i for i in range(n)}
        self.size = [1] * n  
        def find(x:int):

            while x != self.parent[x]:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x
        def union(x, y):
            rx = find(x)
            ry = find(y)

            if self.size[rx] > self.size[ry]:
                self.parent[ry] = rx
                self.size[rx] += self.size[ry]
            else:
                self.parent[rx] = ry
                self.size[ry] += self.size[rx]
        for x , y in connections:
            union(x,y)
        
        components = set()

        for i in range(n):
            components.add(find(i))

        return len(components) - 1

