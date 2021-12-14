class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def pre(root):
            if not root : return 
            curval = root.val
            if curval in range(low,high+1): self.s+= curval
            pre(root.left)
            pre(root.right)
         
        self.s = 0
        pre(root)
        return self.s