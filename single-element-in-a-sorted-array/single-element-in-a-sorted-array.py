class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        
        for i in range(0,len(nums)-1,2):  
           
           
            
            if nums[i] != nums[i+1] : 
                
                if nums[i+1] == nums[i+2] : return nums[i]
                else: return nums[i+1]
        
        return nums[-1]