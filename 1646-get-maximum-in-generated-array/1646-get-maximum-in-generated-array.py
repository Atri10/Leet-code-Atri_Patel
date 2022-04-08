class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n==0:return 0
        
        nums = [] 
        
        nums.append(0)
        nums.append(1)
        
        for i in range(1, (n+1) // 2):
            
            nums.insert(i*2,nums[i])
            nums.insert(1+(i*2),nums[i] + nums[i+1])
        
        return max(nums)