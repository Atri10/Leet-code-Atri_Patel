class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid : return 0
        
        def DFS(i,j,area):
            
            if i < 0 or  i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                
                return area
            
            
            grid[i][j] = 0
            area += 1
            
            area = DFS(i+1,j,area)
            area = DFS(i-1,j,area)
            area = DFS(i,j+1,area)
            area = DFS(i,j-1,area)
            
            return area
        
        area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = max(area , DFS(i,j,0))
                    
        return area
                    
                    
        
            