class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = max(strs)
        b = min(strs)
        for i,v in enumerate(b):
            if a[i] != v : return a[:i]
        return b