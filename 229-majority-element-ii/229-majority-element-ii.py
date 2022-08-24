class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        n = 0
        for i in nums:
            n += 1
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
                
                
        ans = []
        
        for (k,v) in dic.items():
            
            if v > (n / 3):
                ans.append(k)
                
        return ans