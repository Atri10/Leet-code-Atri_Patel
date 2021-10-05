class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n==1: return 1
        if n==2: return 2
        if n==3: return 3
        dp = []
        dp.append(1)
        dp.append(2)
        dp.append(3)
        for i in range(4,n+1):dp.append(dp[-1]+dp[-2])
        return dp[-1]