class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = len(nums)
        arr = []
        for i in range(l):
            temp = 0
            for j in range(l):
              
                if nums[j] < nums[i] : temp += 1
            arr.append(temp)
        
        return arr