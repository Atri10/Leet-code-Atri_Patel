class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxnow,maxall = nums[0],nums[0]
        for i in range(1,len(nums)):
            maxnow = max(maxnow + nums[i],nums[i])
            maxall = max(maxnow,maxall)
        
        return maxall