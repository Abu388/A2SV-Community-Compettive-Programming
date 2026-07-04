# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        v = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            v.append(node.val)
            dfs(node.right)
        dfs(root)
        n = TreeNode(v[0])
        t = n
        for i in range(1, len(v)):
            t.right = TreeNode(v[i])
            t = t.right
        return n