# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mp = defaultdict(int)
        def dfs(node):
            if not node: return
            mp[node.val]+= 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        v = list(mp.values())
        v = max(v)
        res = []
        for k in mp:
            if mp[k] == v:
                res.append(k)
        return res
