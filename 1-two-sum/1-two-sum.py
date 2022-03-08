class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasht= {}
        for i in range(len(nums)):
            b = target - nums[i]
            if b in hasht and i != hasht[b] : return [i,hasht[b]]
            else: hasht[nums[i]] = i