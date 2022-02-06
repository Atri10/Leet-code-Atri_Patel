class Solution:
    def hasPathSum(self, root: Optional[TreeNode], s: int) -> bool:
        if not root: return False
        
        if not root.left and not root.right : return s == root.val
        
        else: return self.hasPathSum(root.left,s-root.val) or self.hasPathSum(root.right,s-root.val)