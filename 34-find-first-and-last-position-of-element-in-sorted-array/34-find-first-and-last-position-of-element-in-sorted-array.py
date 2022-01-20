class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if target in nums:
            idx = nums.index(target)
            c = nums.count(target)
            return [idx,idx+c-1]
        else:
            return [-1,-1]