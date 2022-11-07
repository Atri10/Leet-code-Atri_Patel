class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val
        
        
        L = self.hasPathSum(root.left,targetSum-root.val)
        R = self.hasPathSum(root.right,targetSum-root.val)
        
        return L or R