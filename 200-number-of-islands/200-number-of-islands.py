class Solution:
    def numIslands(self, grid):
        
        if not grid : return 0
         
        
        def DFS(i,j):
            
            if 0 > i or i > len(grid)-1 or j < 0 or j > len(grid[0])-1 or grid[i][j] != "1":
                return
            
            grid[i][j] ="#"
            
            DFS(i+1,j)
            DFS(i,j+1)
            DFS(i-1,j)
            DFS(i,j-1)
            
        
        
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == "1":
                    DFS(i,j)
                    ans += 1
        
        return ans