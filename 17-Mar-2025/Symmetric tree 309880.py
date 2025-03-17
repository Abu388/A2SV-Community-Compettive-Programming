# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root.left
        q = root.right
        def solu(p,q):
            if not q and not p :return True
            if not q or not p: return False
            if q.val != p.val:
                return False
            return (solu(p.left,q.right) and solu(p.right,q.left))

        return solu(p,q)