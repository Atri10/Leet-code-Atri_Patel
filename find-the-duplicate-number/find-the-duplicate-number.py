class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        memo = {}
        
        for i in nums:
            if i in memo:return i
            else: memo[i] = True
            