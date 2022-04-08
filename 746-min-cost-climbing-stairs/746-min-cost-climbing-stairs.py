from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.insert(0,-1)
        
        for i in range(3,len(cost)):
            cost[i] += min(cost[i-1],cost[i-2])
            
        return min(cost[-1],cost[-2])