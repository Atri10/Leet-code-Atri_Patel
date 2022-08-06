class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        
        def back(nums,i,target):
            
            if i >= len(nums):return 0
            
            if target == 0:return 1
            
            if target in memo:
                return memo[target]
            
            res = 0
            
            for k in range(len(nums)):
                if target - nums[k] >= 0:   
                    res += back(nums,k,target - nums[k] )
            
            memo[target] = res
            return memo[target]
        
        return back(nums,0,target)