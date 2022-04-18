class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def rec(root):
            if root:
                arr.append(root.val)
                rec(root.left)
                rec(root.right)
                
        rec(root)     
        arr.sort()
        return arr[k-1] 
                