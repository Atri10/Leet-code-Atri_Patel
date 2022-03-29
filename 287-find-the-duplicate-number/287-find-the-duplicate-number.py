class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        nums.sort()
        dic = {}
        for i in nums:
            if i in dic: return i
            else: dic[i] = True
                
        return False
                