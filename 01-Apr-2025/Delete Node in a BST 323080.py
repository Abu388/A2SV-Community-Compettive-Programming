# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(root):
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right
            curr = root
            left = root.left
            right = root.right
            while left.right:
                left = left.right
            left.right = right

            return curr.left

        if not root:
            return None
        if key == root.val:
            return delete(root)

        cur = root

        while root:
            if key < root.val:
                if root.left and root.left.val == key:
                    root.left = delete(root.left)
                    break
                root = root.left 
            else:
                if root.right and root.right.val == key:
                    root.right = delete(root.right)
                    break
                root = root.right
        return cur


                

                




        search(root)
       












        
        # def solution(root):
        #     cur = root
        #     print(cur.val)
            
        #     if cur.val > key:
        #         solution(cur.left)
        #         if cur == key:
        #             if solution(cur.right.left):
        #                 cur.val = cur.right.left.val
        #                 cur = cur.right.left
        #             elif solution(cur.right):
        #                 cur.val=cur.right.val
        #                 cur=cur.right
        #             else:
        #                 cur = TreeNode(None)
        #     else:
        #         solution(cur.right)

        #         if solution(cur.right.left ):
        #             cur.val = cur.right.left.val
        #             cur = cur.right.left

        #         elif solution(cur.right):
        #                 cur.val=cur.right.val
        #                 cur=cur.right
        #         else:
        #             cur = TreeNode(None)
                
            
        #     return root
        # return solution(root)