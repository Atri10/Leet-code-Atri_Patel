class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = 0
        if len(nums) == 0: return 0 
        for i in range(1,len(nums)):
            if nums[n] < nums[i]:
                n += 1
                nums[n] = nums[i]
        return n+1
      