# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        arr = []
        
        def rec(root):
            
            if root:
                rec(root.left)
                arr.append(root.val)
                rec(root.right)
                
        
        rec(root1)
        rec(root2)
        arr.sort()
        return arr