
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        arr = []
        
        def rec(root):
            
            if root:
                rec(root.left)
                arr.append(root.val)
                rec(root.right)
                
        rec(root)
        arr.sort()
        temp = n = TreeNode(-1)
        
        for i in arr:
            temp.left = None
            temp.right = TreeNode(i)
            temp = temp.right
            
        return n.right