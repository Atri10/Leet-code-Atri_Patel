class Solution:
    def frequencySort(self, s: str) -> str:
        
        dic = {}
        
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        dic = dict(sorted(dic.items(), reverse = True, key=lambda x:x[1]))
        
        ans = ""
        for k,v in dic.items():
            ans += k*v
        
        return ans