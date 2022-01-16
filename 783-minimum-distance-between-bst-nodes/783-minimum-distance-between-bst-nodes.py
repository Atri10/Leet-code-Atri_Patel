# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        arr = []
        def rec(root):
            if root:
                rec(root.left)
                arr.append(root.val)
                rec(root.right)
                
        def getdis(arr):
            return min(b-a for a,b in zip(arr,arr[1:]))
        
        rec(root)
        return getdis(arr)