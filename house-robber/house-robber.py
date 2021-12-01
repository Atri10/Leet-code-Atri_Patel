class Solution:
    def rob(self, nums: List[int]) -> int:
        last_house = 0
        cur_house = 0
        for n in nums:last_house,cur_house = cur_house,max(cur_house,last_house+n)
        return cur_house