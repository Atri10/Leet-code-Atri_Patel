class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        x = map(sum,accounts)
        return max(x)