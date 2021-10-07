class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def DFS(i,j,idx,visited):
            if (i,j) in visited or i<0 or j<0 or j>=len(board[0]) or i>=len(board) or word[idx]!=board[i][j]:
                return False
            if idx==len(word)-1:return True
            visited.add((i,j))
            left = DFS(i,j-1,idx+1,visited)
            right = DFS(i,j+1,idx+1,visited)
            up = DFS(i-1,j,idx+1,visited)
            down = DFS(i+1,j,idx+1,visited)
            visited.discard((i,j))
            return left or right or up or down
            
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    visited = set()
                    if DFS(i,j,0,visited):return True
                
        return False