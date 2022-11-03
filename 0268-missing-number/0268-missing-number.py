class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        dic = {}
        
        for i in nums:
            dic[i] =True
        
        n = len(nums)
        mis = 0
        for i in range(n+1):
            if i not in nums: mis = i
        return mis