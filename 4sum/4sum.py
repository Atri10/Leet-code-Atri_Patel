class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []
        nums.sort()
        for i in range(0,len(nums)-3):
            for j in range(i+1,len(nums)-2):
                
                l = j+1
                r = len(nums) - 1
                while l < r:
                    if nums[l]+nums[r]+nums[i]+nums[j]==target:
                        T = [nums[l],nums[r],nums[i],nums[j]]
                        if T not in ans:ans.append(T)
                        l+=1
                        r-=1
                    elif nums[l]+nums[r]+nums[i]+nums[j] < target:l+=1
                    else:r-=1
        return ans
                        