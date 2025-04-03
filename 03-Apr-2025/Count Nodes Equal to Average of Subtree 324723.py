# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        
        def solu(node):
            nonlocal count
            if not node:
                return (0, 0)  

            l_sum, l_count = solu(node.left)
            r_sum, r_count = solu(node.right)
            
            t_sum = l_sum + r_sum + node.val
            t_count = l_count + r_count + 1

            
            if node.val == t_sum // t_count:
                count += 1

            return (t_sum, t_count)
        
        solu(root)  
        return count


            