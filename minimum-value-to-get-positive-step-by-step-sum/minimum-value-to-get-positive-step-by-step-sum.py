class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minval = 0
        pre = 0
        for i in nums:
            pre += i
            minval = min(pre,minval)
        return 1-minval