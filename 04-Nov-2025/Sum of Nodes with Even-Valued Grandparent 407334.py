# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        res = 0
        def bfs(node ):# gp
            nonlocal res
            q = deque([])
            if node.left: #parent
                q.append(node.left)
            if node.right:
                q.append(node.right)

            while q:
                parent = q.popleft()
                if parent.left: #parent
                    res += parent.left.val
                if parent.right:
                    res += parent.right.val

        def travers(node):
            if node.val % 2 == 0:
                print(node.val)
                bfs(node)
            
            if node.left: #parent
                travers(node.left)
            if node.right:
                travers(node.right)

        travers(root)

        return res