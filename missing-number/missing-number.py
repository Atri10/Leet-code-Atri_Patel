class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        mis = 0
        for i in range(n+1):
            if i not in nums: mis = i
        return mis