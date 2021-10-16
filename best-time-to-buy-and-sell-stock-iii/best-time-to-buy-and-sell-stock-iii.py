class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        b1 = 20000000
        s1 = -1
        b2 = 20000000
        s2 = -1
        
        for price in prices:
            
            b1 = min(b1,price)
            s1 = max(s1,price-b1)
            b2 = min(b2,price - s1)
            s2 = max(s2,price - b2)
            
        return s2
        