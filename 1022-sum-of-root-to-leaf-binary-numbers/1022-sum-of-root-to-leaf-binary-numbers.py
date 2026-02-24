class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = []
        path = []

        def dfs(node):
            if not node:
                return
            
            path.append(node.val)

            # Only append when it's a leaf
            if not node.left and not node.right:
                res.append(path.copy())
            else:
                dfs(node.left)
                dfs(node.right)

            path.pop()

        dfs(root)
        fin = [int(''.join(map(str, i)), 2) for i in res]
        
        return sum(fin)