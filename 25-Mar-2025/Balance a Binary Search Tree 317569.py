# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        
        def solu(root):
            if not root:
                return
            
            solu(root.left)
            arr.append(root.val)
            solu(root.right)
        solu(root)
        def tree(left,right):
           
            if left > right:
                return None
            mid = (left+right)//2
            node = TreeNode(arr[mid])
            node.left = tree(left,mid-1)
            node.right = tree(mid+1,right)
            return node
        return tree(0, len(arr)-1)
        
        

        


        