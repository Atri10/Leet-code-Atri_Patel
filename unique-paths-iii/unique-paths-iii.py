class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        sx,sy,zero,m,n = 0,0,0,len(grid),len(grid[0])
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 : zero += 1
                elif grid[i][j] == 1 : sx,sy = i,j
                else:continue
        
        
        def DFS(x,y,zero):
            
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == -1 : return 0
            
            if grid[x][y] == 2 : 
                if zero == -1:return 1 
                else: return 0
    
            grid[x][y] = -1
            zero -= 1
            
            total = DFS(x+1,y,zero) +  DFS(x-1,y,zero) + DFS(x,y+1,zero) + DFS(x,y-1,zero)
            
            grid[x][y] = 0
            zero += 1
            
            return total
            
        return DFS(sx,sy,zero)