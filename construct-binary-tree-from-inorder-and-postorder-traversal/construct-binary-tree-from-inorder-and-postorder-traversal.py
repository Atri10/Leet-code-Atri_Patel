class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dic = {}
        for (i,v) in enumerate(inorder):dic[v] = i

        def rec(pb,pe,ib,ie):
            if pe - pb <= 0 : return None
            idx = dic[postorder[pe-1]]
            root = TreeNode(inorder[idx])
            root.left = rec(pb,pb+idx-ib,ib,idx)
            root.right = rec(pe-ie+idx,pe-1,idx+1,ie)
            return root
        
        return rec(0,len(postorder),0,len(inorder))