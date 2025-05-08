# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

from heapq import *
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        heap = []
        parent = [i for i in range(n+1)]
        size = [1] * (n + 1)

        def find(x):
            stk  = []
            while parent[x] != x:
                stk.append(x)
                x = parent[x]        
            while stk:
                parent[stk.pop()] = x
            return parent[x]
        def union(x,y):
            xu = find(x)
            yu = find(y)     
            if size[xu] > size[yu]:
                size[xu] += size[yu]
                parent[xu] = yu
            else:        
                size[yu] += size[xu]
                parent[yu] = xu

        
        for i in range(n):
            for j in range(i,n):
                x1 =  points[i][0]
                x2 =  points[j][0]
                y1 =  points[i][1]
                y2 =  points[j][1]
                val = abs(x1-x2) + abs(y1 - y2)
                heappush(heap, (val ,i , j))
        res = 0
        while heap:
            v , a , b = heappop(heap)
            if find(a) != find(b):
                union(a,b)
                res += v
        return res
        