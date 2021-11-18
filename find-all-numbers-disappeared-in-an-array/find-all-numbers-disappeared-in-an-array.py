class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        mem = {}
        ans = []
        for i in nums : mem[i] = True
        for i in range(1,len(nums)+1):
            if i not in mem : ans.append(i) 
        return ans