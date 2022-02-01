class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Min = float('inf')
        Profit = 0
        for CP in prices:
            Min = min(Min,CP)
            Profit = max(Profit,CP-Min)
        return Profit