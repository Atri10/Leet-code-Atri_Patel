class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = float("inf")
        profit = 0
        for price in prices:
            if minn > price : minn = price
            if price - minn > profit : profit = price - minn
        return profit