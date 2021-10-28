class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        def inorder(root):
            if root:
                inorder(root.left)
                self.ans.append(root.val)
                inorder(root.right)

        inorder(root)
        return self.ans
            
            
            