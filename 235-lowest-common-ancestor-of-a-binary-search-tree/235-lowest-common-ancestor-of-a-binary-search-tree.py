# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        big = max(p.val, q.val)
        small = min(p.val, q.val)
        
        while root : 
            if root.val > big:root = root.left
            elif root.val < small:root = root.right
            else: return root
            
        return None