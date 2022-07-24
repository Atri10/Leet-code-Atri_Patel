class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        dic = {}
        
        for i in range(len(nums)):
            num = nums[i]
            el = target - num
            
            if el in dic:
                return [dic[el],i]
            
            if num not in dic: dic[num] = i