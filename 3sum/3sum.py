class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        triplets = []
       
       
        for i in range(len(nums)-2):
            
            left = i+1
            right = len(nums)-1
            print(i,left,right)
            while left < right:
                T = nums[i] + nums[left] + nums[right]
                if T ==0:
                    ans = [nums[i],nums[left],nums[right]]
                    if ans not in triplets :triplets.append(ans)
                    left+=1
                    right -=1
                
                elif T>0:right -=1
                else: left+=1
        
        
        return triplets
                    
                