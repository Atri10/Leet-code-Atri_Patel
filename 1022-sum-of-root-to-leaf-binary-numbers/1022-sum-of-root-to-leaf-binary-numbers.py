class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def rec(root,s):
            if not root : return 0
            s = 2 * s + root.val
            if not root.left and not root.right : return s
            return rec(root.left,s) + rec(root.right,s)
        return rec(root,0)