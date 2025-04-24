# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r,c,n):
            value = grid[r][c]
            all_same = True
            for i in range(r,r+n):
                for j in range(c,c+n):
                    if grid[i][j] != value:
                        all_same = False
                        break
                if not all_same:
                    break
            n = n // 2
            if all_same:
                return Node(val=bool(value), isLeaf=True)
            return Node(
                val = True,
                isLeaf = False,
                topLeft = dfs(r, c , n),
                topRight = dfs(r, c + n , n),
                bottomLeft = dfs(r + n, c , n),
                bottomRight = dfs(r + n, c + n, n)
            )
        return dfs(0,0,len(grid))