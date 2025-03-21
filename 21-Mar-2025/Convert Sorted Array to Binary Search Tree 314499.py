# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#          self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def mg(nums):
            if len(nums) ==0:
                return None
            n = len(nums)
            m = n//2
            
            l = mg(nums[:m])
            r = mg(nums[m+1:])

            return TreeNode(nums[m],l, r)
        return mg(nums)
        