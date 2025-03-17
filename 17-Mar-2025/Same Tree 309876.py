# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def solu(q,p):
            if not q and not p:
                return True
            if not q or not p:
                return False
            if q.val != p.val:
                return False

            
            return (solu(q.left,p.left) and solu(q.right,p.right) )

            
            
        
        return solu(q,p)