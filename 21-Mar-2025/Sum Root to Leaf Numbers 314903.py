# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        total = 0
        def solu(root, cur):
            nonlocal total
            if not root:return 0
            cur += str(root.val)
            if not root.left and not root.right:
                total +=(int(cur))                
                return 

            l=solu(root.left, cur)
            r=solu(root.right, cur)
            
            
        solu(root, '')
        
        return total