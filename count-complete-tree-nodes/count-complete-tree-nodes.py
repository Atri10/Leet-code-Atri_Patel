# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def preorder(root):
            if root:
                self.count += 1
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return self.count