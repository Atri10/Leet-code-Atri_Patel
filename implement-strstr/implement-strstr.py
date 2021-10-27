class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if not needle:return 0
        
        if len(needle) > len(haystack):return -1
        
        if haystack == needle:return 0
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                main = haystack[i:len(needle)+i]
                if main == needle:return i
        return -1