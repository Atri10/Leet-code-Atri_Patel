class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dic = {}
        
        for i in nums:
            if i in dic : dic[i] = dic[i] + 1
            else: dic[i] = 1
        
        return max(zip(dic.keys(),dic.values()),key = lambda i : i[1])[0]