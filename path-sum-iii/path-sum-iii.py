class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def Preorder(root,cursum):
            nonlocal ans
            if not root:return
            cursum += root.val
            if cursum == targetSum: ans += 1
            ans += h[cursum-targetSum]
            h[cursum]+=1
            Preorder(root.left,cursum)
            Preorder(root.right,cursum)
            h[cursum]-=1
        ans = 0
        h = defaultdict(int)
        Preorder(root,0)
        return ans
    
