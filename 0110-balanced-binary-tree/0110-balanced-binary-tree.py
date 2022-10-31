# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        self.isBal = True
        
        def rec(root):
            
            if not root:
                return 0
                
            L = rec(root.left)
            R = rec(root.right)
                
            if abs(L-R) > 1:
                self.isBal = False
                    
            return max(L,R) + 1
        
        rec(root)
        return self.isBal