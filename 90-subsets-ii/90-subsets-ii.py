class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subsets = []
        
        def sub(i):
            
            if i >= len(nums):
                temp = sorted(res.copy())
                if temp not in subsets:
                    subsets.append(temp)
                return 
            
            res.append(nums[i])
            sub(i+1)
            res.pop()
            sub(i+1)
            
        
        sub(0)
        return subsets