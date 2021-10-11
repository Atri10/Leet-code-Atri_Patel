
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

            
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        self.maxx = 1
        def DFS(root):
            if not root:return 0
            left = DFS(root.left)
            right = DFS(root.right)
            self.maxx = max(self.maxx,left+right+1)
            return 1 + max(left,right)
            
       
        DFS(root)
        
        return self.maxx-1
        