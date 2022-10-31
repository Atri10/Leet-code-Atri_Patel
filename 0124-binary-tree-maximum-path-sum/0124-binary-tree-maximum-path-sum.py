# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        def rec(root):
            
            if not root:
                return 0
            
            L = rec(root.left)
            R = rec(root.right)
            self.MAX = max(self.MAX, L + R + root.val)
            return max((max(L,R) + root.val),0)
        
        self.MAX = - float('inf')
        rec(root)
        return self.MAX