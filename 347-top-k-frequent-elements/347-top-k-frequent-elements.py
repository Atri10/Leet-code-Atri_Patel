class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}
        
        for i in nums:
            if i in dic: dic[i] = dic[i] + 1
            else: dic[i] = 1
                
        d = sorted(dic.items(),key = lambda x : x[1], reverse = True)
        ans = [a for a,b in d[:k]]
        return ans