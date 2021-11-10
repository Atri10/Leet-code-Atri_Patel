class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2 : return 0
        s1,s2 = -prices[0],0
        for p in prices:
            s1 = max(s1,s2-p)
            s2 = max(s2,s1+p)
        
        return s2