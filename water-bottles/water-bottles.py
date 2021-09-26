class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            remaining = numBottles%numExchange
            numBottles = numBottles // numExchange
            ans += numBottles
            numBottles += remaining
        return int(ans)
        