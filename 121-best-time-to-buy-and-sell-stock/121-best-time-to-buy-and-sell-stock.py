class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxCur = 0
        maxFar = 0
        
        for i in range(1,len(prices)):
            maxCur += prices[i] - prices[i-1]
            print(maxCur,maxFar)
            maxCur = max(0,maxCur)
            maxFar = max(maxCur,maxFar)
            
        
        return maxFar