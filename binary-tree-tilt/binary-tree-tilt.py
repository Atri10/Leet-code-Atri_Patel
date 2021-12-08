# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def rec(root):
            
            if not root : return (0,0)
            
            left = rec(root.left)
            right = rec(root.right)
            
            return (left[0] + right[0] + root.val,abs(left[0] - right[0]) + left[1] + right[1])
        
        return rec(root)[1]