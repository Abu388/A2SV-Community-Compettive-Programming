# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
     
        def dfs(root):
            if not root.left and not root.right:
                return 1
            l = r = 0
            if root.left :   
                
                l = dfs(root.left)
            if root.right:
                
                r = dfs(root.right)
            if r == 0:
                return l + 1
            elif l == 0:
                return r + 1
            else:
                return min(l, r) + 1
        return dfs(root)
