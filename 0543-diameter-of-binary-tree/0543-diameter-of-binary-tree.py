# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.MAX = -1
        
        def rec(root):
            
            if root:
                
                L = rec(root.left)
                R = rec(root.right)
                self.MAX = max(self.MAX, L+R+1)
                return 1 + max(L,R)
            
            else:
                return 0
            
        rec(root)
        return self.MAX - 1