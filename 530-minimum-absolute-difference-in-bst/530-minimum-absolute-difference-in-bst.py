class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        arr = []
        def dfs(root):
            if root:
                dfs(root.left)
                arr.append(root.val)
                dfs(root.right)
                
        dfs(root)    
        return min(b-a for a,b in (zip(arr,arr[1:])))