class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = sum(i%2 for i in position)
        return min(odd,len(position)-odd)