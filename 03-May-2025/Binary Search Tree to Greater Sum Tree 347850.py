# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        r = float('-inf')
        def travers(root):
            nonlocal r
            r = max(r,root.val)
            if root.left:
                travers(root.left)
            if root.right:
                travers(root.right)
        travers(root)
        parent = [0] * (r + 1)
        def count(root):
            parent[root.val] += 1
            if root.left:
                count(root.left)
            if root.right:
                count(root.right)
        count(root)
        
        for i in range(1,len(parent)):
            parent[i] *= i
        
        def final(root):
            total = 0
            for i in range(root.val+1,len(parent)):
                total += parent[i]
            root.val += total 
            
            if root.left:
                final(root.left)
            if root.right:
                final(root.right)
        final(root)
        return root