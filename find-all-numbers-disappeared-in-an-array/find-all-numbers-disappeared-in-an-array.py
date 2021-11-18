class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        mem = {}
        ans = []
        for i in nums : mem[i] = True
            
        for i in range(len(nums)):
            if (i+1) not in mem : ans.append(i+1) 
                
        return ans