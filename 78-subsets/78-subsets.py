class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []
        def subset(i):
            if i >= len(nums):
                sub.append(ans.copy())
                return
            
            ans.append(nums[i])
            subset(i+1)
            ans.pop()
            subset(i+1)
              
        subset(0)
        return sub