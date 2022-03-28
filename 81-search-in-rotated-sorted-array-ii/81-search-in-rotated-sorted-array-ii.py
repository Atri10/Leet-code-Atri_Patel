class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        ans = False
        for i in nums:
            if i == target:ans = True
                
        return ans