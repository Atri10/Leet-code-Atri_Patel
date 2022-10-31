# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root in [p,q]:
            return root
        
        L, R = None, None
        if root.left:
            L = self.lowestCommonAncestor(root.left,p,q)
        
        if root.right:
            R = self.lowestCommonAncestor(root.right,p,q)
            
        
        if L and R:
            return root
        
        if L or R:
            return L or R