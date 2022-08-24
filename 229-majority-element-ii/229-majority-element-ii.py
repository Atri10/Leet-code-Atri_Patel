class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        n = len(nums)
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
                
                
        ans = []
        
        for (k,v) in dic.items():
            
            if v > (n / 3):
                ans.append(k)
                
        return ans