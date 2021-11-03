class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic = {}
        for i in range(len(s)):dic[indices[i]] = s[i]      
        a = list(dic.keys())
        ans = ""
        k = sorted(dic)
        for i in k:ans += dic[i]
        return (ans)