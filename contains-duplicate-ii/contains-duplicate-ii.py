class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memo = {}
        for i in range(len(nums)):    
            if nums[i] in memo and abs(memo[nums[i]] - i) <=k : return True          
            else:memo[nums[i]]=i
        return False