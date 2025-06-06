# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
     
        cur=0
        def solu(root,cur):
            if not root:
                return

            cur=root.val


            if cur == val:
                return root
            if cur > val:
                left=solu(root.left, cur)
                return left
            else:
                right=solu(root.right, cur)
                return right


           
            
            
      
        return solu(root, cur)


        