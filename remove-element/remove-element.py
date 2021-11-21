class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        l = len(nums)
        for i in range(l):
            if nums[i] == val : c += 1
            else : nums[i-c] = nums[i];
        
        return l - c