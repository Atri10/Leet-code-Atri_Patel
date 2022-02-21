class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        ans = nums[len(nums)//2]
        return ans