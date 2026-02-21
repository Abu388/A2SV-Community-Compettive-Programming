# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        value = defaultdict(list)
        res = []
        q = deque([(root ,  0)])
        while q:
            node , c = q.popleft()
            value[c].append(node.val)
            if node.left:
                q.append((node.left, c + 1))
            if node.right:
                q.append((node.right, c + 1))
        
        for v in value.values():
            res.append(sum(v) / len(v))
        return res

