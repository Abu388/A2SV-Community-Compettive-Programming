# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans =[]
        def pre(root):
            if not root:
                return
            ans.append(root.val)
            pre(root.left)
            pre(root.right)
        pre(root)
        return ans









        # cur,stack=root,[]
        # res=[]
        
        # while cur or stack:
        #     if cur:
        #         res.append(cur.val)
        #         stack.append(cur.right)
        #         cur=cur.left
        #     else:
        #         cur= stack.pop()
                
        # return res
    
        