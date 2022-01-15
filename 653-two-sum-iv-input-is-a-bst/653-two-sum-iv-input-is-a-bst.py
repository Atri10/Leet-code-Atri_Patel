class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        
        def towsum(arr):
            
            dic = {}
            
            for i in arr:
                x = k - i
                if x in dic : return True
                else : dic[i] = True
            return False
                    
        def rec(root):
            if root:
                rec(root.left)
                arr.append(root.val)
                rec(root.right)
                
        rec(root)
        return towsum(arr)