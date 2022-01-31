# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        q = collections.deque([(root, 1)])
        
        while q:
            node,level = q.popleft()
            
            if node:
                if not node.left and not node.right: 
                    return level
                else:
                    q.append((node.left,level+1))
                    q.append((node.right,level+1))