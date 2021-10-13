# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        
        def subtree(lo, hi):
            if lo >= hi: return None
            rootval = preorder[lo]
            root = TreeNode( rootval )
            mid = bisect.bisect_left(preorder, rootval, lo+1, hi) 
            root.left = subtree(lo+1, mid)
            root.right = subtree(mid, hi)
            return root
        
        return subtree( 0, len(preorder) )