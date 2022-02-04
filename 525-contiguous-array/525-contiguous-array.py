class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        c = 0
        res = 0
        dic = {0:-1}
        
        for i in range(len(nums)):
            
            n = nums[i]
            
            if n == 1 : c += 1
            else: c -= 1

                
            if c in dic : res = max(res, i - dic[c])
                
            else:dic[c] = i
                
        return res