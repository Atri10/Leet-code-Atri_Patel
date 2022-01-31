# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        p = root.left
        q = root.right
        
        def rec(p,q):
            if not p or not q: return p == q
            if p.val != q.val: return False
            return rec(p.left, q.right) and rec(p.right, q.left)
        
        return rec(p,q)