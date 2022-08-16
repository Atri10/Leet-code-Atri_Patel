class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = nums.count(0)

        for i in range(zero):
            nums.remove(0)
            nums.append(0)
            