class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if val == root.val:return root
            if val > root.val:root = root.right
            else:root = root.left