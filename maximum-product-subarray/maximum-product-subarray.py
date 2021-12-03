class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        cmaxx,cminn = 1,1
        ind = nums[0]
        
        for num in nums:
            v = [num,cminn*num,cmaxx*num]
            cmaxx,cminn = max(v), min(v)
            ind = max(ind,cmaxx)
            
        return ind