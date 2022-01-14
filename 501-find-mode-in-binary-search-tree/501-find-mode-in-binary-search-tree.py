class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        dic = {}
        
        def pre(root):
            
            if root:
                pre(root.left)
                
                if root.val in dic : dic[root.val] =  dic[root.val] + 1
                else : dic[root.val] = 1
                
                pre(root.right)
                
        pre(root)
        maxx = max(dic.values())
        ans = [x for x,y in dic.items() if y == maxx ]
        return ans