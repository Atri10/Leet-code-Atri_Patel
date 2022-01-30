class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
    
        def rev(nums,l,r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l = l + 1
                r = r - 1
        
        
        
        ll = len(nums)
        k = k % ll;
        rev(nums,0,ll-k-1)
        rev(nums,ll-k,ll-1)
        rev(nums,0,ll-1)
        
        