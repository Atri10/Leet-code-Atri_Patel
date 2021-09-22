class Solution:
    def arraySign(self, nums: List[int]) -> int:
        countneg = 0
        for i in nums:
            if 0>i:countneg +=1
            elif i==0:return 0
        if countneg%2==0:return 1
        else:return -1