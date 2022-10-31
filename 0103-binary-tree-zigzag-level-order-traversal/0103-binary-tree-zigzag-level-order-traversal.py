# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        level, ans = [root] , []
        
        while level:
            
            ans.append([node.val for node in level])
            
            temp = []
            
            for node in level:
                temp.extend([node.left,node.right])
            
            level = [leaf for leaf in temp if leaf]
            

        for i in range(1,len(ans),2):
            ans[i] = ans[i][::-1]
            
        return ans