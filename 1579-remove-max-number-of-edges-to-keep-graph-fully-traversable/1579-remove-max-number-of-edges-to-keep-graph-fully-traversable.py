class UF:
    def __init__(self,n):
        self.component = n
        self.par = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
    
    def find(self, x):
        stk = []
        while self.par[x] != x:
            stk.append(x)
            x = self.par[x]
        while stk:
            self.par[stk.pop()] = x
        return x

    def union(self, u , v):
        x , y = self.find(u) , self.find(v)
        if x == y: # which means they have the same parent
            return False
        if self.rank[x] > self.rank[y]:
            self.par[y] = x
            self.rank[x] += self.rank[y]
        else:
            self.par[x] = y
            self.rank[y] += self.rank[x]
        self.component -= 1
        return True
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        removed = 0
        alice ,bob = UF(n) , UF(n) 
        for t , u , v in edges:
            if t == 3:
                usedAlice = alice.union(u, v)
                usedBob = bob.union(u,v)
                if not usedAlice and not usedBob:
                    removed += 1

        for t , u , v in edges:
            if t == 1:
                if not alice.union(u,v):
                    removed += 1
        for t , u , v in edges:
            if t == 2:
                if not bob.union(u,v):
                    removed += 1 
        if alice.component != 1 or bob.component != 1 :
            return -1
        return removed
        