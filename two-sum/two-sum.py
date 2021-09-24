class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            temp = target - n
            if temp in d:return [d[temp], i]
            else:d[n] = i
                

            