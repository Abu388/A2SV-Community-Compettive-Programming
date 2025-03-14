# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        arr=[]
        cur=''
        if not root:
            return arr
        def solu(root,cur):
            if not root:
                return
            if cur == '':
                cur+=str(root.val)
            else:
                cur+='->'+str(root.val)
            
            if not root.left and not root.right:
                arr.append(cur)
            
            left=solu(root.left,cur)
            right=solu(root.right,cur)
            

        solu(root,cur)
        return arr


            
        