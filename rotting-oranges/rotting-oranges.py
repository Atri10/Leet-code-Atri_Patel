from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        c = len(grid)
        r = len(grid[0])
        rotten_pos = deque()
        fresh_count = 0
        
        for i in range(c):
            for j in range(r):
                if grid[i][j] == 2 : rotten_pos.append((i,j))
                elif grid[i][j] == 1 : fresh_count += 1

        Directions = [(1,0),(-1,0),(0,1),(0,-1)]
        levels = 0
        
        while rotten_pos:
            levels += 1
    
            for i in range(len(rotten_pos)):
                x,y = rotten_pos.popleft()
                for dx,dy in Directions:
                    if 0 <= x+dx < c and 0 <= y+dy < r and grid[x+dx][y+dy] == 1:
                        fresh_count -= 1
                        grid[x+dx][y+dy] = 2
                        rotten_pos.append((x+dx,y+dy))
                        
        return -1 if fresh_count != 0 else max(levels-1,0)