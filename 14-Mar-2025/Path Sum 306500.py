# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    
        def solu(root,cur):
            
            if not root:
                return False
            cur += root.val
            if not root.left and not root.right:
                return cur == targetSum
            return solu(root.left , cur) or solu(root.right , cur)
        return solu(root , 0)


       




        
            
            