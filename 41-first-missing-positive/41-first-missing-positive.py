class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        point = 1
        for i in nums:
            if i == point:point += 1    
        return point