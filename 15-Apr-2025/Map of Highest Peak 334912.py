# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque([])
        visited = set()
        d  = [(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(row , col):
            return 0 <= row < len(isWater) and 0 <= col < len(isWater[0])
        def bfs(r,c):
            for nr , nc in d:
                newr = r + nr
                newc = c + nc
                if inbound(newr,newc):
                    if isWater[newr][newc] != 1 and (newr,newc) not in visited:
                        q.append((newr,newc,1))
                        visited.add((newr,newc))
                        isWater[newr][newc] = 1

        row = len(isWater)
        col = len(isWater[0])
        for r in range(row):
            for c in range(col):
                if isWater[r][c] == 1 and (r,c) not in visited:
                    visited.add((r,c))
                    isWater[r][c] = 0
                    bfs(r,c)
        
        while q:
            u , v ,m = q.popleft()
            for nr , nc in d:
                newr = u + nr
                newc = v + nc
                if inbound(newr,newc):
                    if (newr,newc) not in visited:
                        q.append((newr,newc,m + 1))
                        visited.add((newr,newc))
                        isWater[newr][newc] = m + 1


        return isWater
       