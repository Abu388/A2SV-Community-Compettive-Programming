# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(org, clo, targ):
            if not org:
                return None
            if org == targ:
                return clo
            left = dfs(org.left, clo.left, targ)
            if left:
                return left
            return dfs(org.right, clo.right, targ)
        return dfs(original, cloned, target)