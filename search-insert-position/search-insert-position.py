class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        

            
        low = 0
        high = len(nums)
            
        while low < high:
                
            mid = (high + low) // 2
            if nums[mid] == target : return mid
            elif nums[mid] > target : high = mid
            else: low = mid + 1
                
           
        return low