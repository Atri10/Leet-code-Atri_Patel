class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur = 0
        for i in nums:
            if cur < 0 :cur = 0
            cur += i
            ans = max(ans,cur)
        return ans