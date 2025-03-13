# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def solu(root):
            
            if not root:
                return 0 
            left=1+solu(root.left)
            right=1+solu(root.right)
            
            return max(right,left)
            
            
        return solu(root)

       
        