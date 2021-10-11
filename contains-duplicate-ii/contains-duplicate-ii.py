class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memo = {}
        minn = 999999
        maxx = 0
        arr = []
        for i in range(len(nums)):
            if nums[i] in memo:
                minn = memo[nums[i]]
                maxx = max(maxx,i)
                memo[nums[i]] = i
                arr.append(abs(minn-maxx) <= k)
            else:memo[nums[i]] = i 
        return (True in arr)