class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        maxx = -float('inf')
        while i < j :
            maxx = max(maxx,nums[i]+nums[j])
            i += 1
            j -= 1
        return maxx