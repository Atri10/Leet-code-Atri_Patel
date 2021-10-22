class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        ans = ""
        for i in s:
            if i not in hashmap:hashmap[i] = 1
            else:hashmap[i] = hashmap[i] + 1
        for i, (k,v) in enumerate(sorted(hashmap.items(),key=lambda x:x[1],reverse=True)):ans += (k*v)
        return ans