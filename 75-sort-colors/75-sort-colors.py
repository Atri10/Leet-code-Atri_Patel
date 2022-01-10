class Solution:
    def sortColors(self, nums: List[int]) -> None:    
        zero = 0
        one =  0
        two = 0
        
        for i in nums:
            if i == 0 : zero += 1
            if i == 1 : one += 1
            if i == 2 : two += 1
    
        for i in range(zero):nums[i] = 0
        for i in range(zero,zero+one):nums[i] = 1
        for i in range(zero+one,two+one+zero):nums[i] = 2