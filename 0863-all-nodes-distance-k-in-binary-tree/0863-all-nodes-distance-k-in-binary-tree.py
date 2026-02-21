# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
   
        graph = defaultdict(list)
        def build(root):
            if not root:
                return 
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                build(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                build(root.right)
        build(root)
        res = []
        def dfs(node , num):
            nonlocal k ,target
            if num == k:
                res.append(node)
                return

            for nig in graph[node]:
                if nig != target.val:
                    dfs(nig , num +  1)


        dfs(target.val, 0) 
        
        return res