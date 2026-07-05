# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        y , x = [], []
        def dfs(node):
            nonlocal y
            if  not node.left and not node.right:
                y.append(str(node.val))
                return
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        
        dfs(root1)
        val = y
        y = x
        dfs(root2)
        val2 = y
     
        return val == val2


        