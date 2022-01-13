# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def rec(l,r):
            m = (l+r)//2
            if l>r : return None
            root = TreeNode(nums[m])
            root.left = rec(l,m-1)
            root.right = rec(m+1,r)
            return root
        
        return rec(0,len(nums)-1)