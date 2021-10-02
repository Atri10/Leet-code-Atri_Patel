from functools import cache
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        @cache
        def rec(i,j):
            if i==m or j==n:return 100000000
            if i==m-1 and j==n-1:
                if dungeon[i][j]<=0:return 1-dungeon[i][j]
                else:return 1
            goright = rec(i,j+1)
            godown = rec(i+1,j)
            minhealth = min(goright,godown) - dungeon[i][j]
            if minhealth <= 0:return 1
            else: return minhealth 
        
        
        return rec(0,0)
            