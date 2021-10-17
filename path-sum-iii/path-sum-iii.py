# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        self.DFS(root,targetSum)
        return self.paths
    
    
    def DFS(self,root,target):
        if not root:return
        self.pathfunc(root,target)
        self.DFS(root.right,target)
        self.DFS(root.left,target)
        
    def pathfunc(self,root,target):
        if not root:return 
        if root.val == target : self.paths += 1
        self.pathfunc(root.right,target-root.val)
        self.pathfunc(root.left,target-root.val)