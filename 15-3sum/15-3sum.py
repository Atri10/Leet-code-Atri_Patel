class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        
        for i in range(len(nums)):
            dic = {}
            for j in range(i+1,len(nums)):
                
                if -(nums[i] + nums[j]) in dic:
                    res = sorted([nums[i],nums[j],-(nums[i] + nums[j])])
                    
                    if res not in ans:
                        ans.append(res)
                    
                else:
                    dic[nums[j]] = j
                    
        return ans