class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        queue = collections.deque([root])
        level = 0
        
        while queue:
            
            curLength = len(queue)
            
            for i in range(curLength):
                
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            level += 1
            
        return level