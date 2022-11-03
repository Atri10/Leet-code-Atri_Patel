class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        dic = {}
        n = len(nums)
        for i in nums:
            dic[i] =True
        
        del(nums)
        mis = 0
        for i in range(n+1):
            if i not in dic: mis = i
        return mis