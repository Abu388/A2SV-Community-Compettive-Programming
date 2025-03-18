# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def solu(node,cur_min,cur_max):
            if not node:
                return cur_max - cur_min
            cur_min = min(cur_min, node.val)
            cur_max = max(cur_max, node.val)
            
            left  = solu(node.left, cur_min, cur_max)
            right = solu(node.right, cur_min, cur_max)

            return max(left,right)
        return solu(root, root.val, root.val)










        # #value assign
        # res_max =  root.val
        # res_min = root.val
        # res_max2 = root.val
        # res_min2 = root.val

        # #moves
        # left_mov = root.left
        # right_mov = root.right
        # #function of left
        # def solution_left(left_mov):
        #     nonlocal res_max, res_min
        #     if not left_mov:
        #         return 
            
        #     res_max = max(res_max, left_mov.val)
        #     res_min = min(res_min, left_mov.val)
            
        #     solution_left(left_mov.left)
        #     solution_left(left_mov.right)
        # #function of right
        # def solution_right(right_mov):
        #     nonlocal res_max2, res_min2
        #     if not right_mov:
        #         return 
            
        #     res_max2 = max(res_max2, right_mov.val)
        #     res_min2 = min(res_min2, right_mov.val)
            
        #     solution_right(right_mov.left)
        #     solution_right(right_mov.right)
        # #final answer 
        # solution_left(left_mov)
        # solution_right(right_mov)
        # print(res_max, res_min)
        
        # return max(abs(res_max2-res_min2),abs(res_max-res_min))