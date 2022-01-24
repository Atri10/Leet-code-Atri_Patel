class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        l = 0
        r = len(s) - 1
        
        while r >= l:
            
            s[l],s[r] = s[r],s[l]
            l = l + 1
            r = r - 1