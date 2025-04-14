# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root])
        target = root.val
        while q:
            node = q.popleft()
            if node.val != target:
                return False
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return True
