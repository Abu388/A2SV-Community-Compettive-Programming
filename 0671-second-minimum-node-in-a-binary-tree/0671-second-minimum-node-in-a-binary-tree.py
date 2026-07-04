# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        v = set()
        def dfs(node):
            if not node:
                return 
            v.add(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        if len(v) == 1:
            return -1
        
        c = 1
        for i in sorted(v):
            if c == 2:
                return i
            c += 1