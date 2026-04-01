class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def mt(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            
            return mt(root.left, subRoot.left) and mt(root.right, subRoot.right)
        
        def search(root):
            if not root:
                return False
            
            if root.val == subRoot.val and mt(root, subRoot):
                return True
            
            return search(root.left) or search(root.right)
        
        return search(root)