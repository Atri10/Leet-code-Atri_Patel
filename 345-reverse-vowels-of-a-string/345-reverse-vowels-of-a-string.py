class Solution:
    def reverseVowels(self, s: str) -> str:
        
        l = 0
        r = len(s) - 1
        vol = ["a","e","i","o","u","A","E","I","O","U"]
        
        s = list(s)
        
        while r > l:
            
            while l < r and s[l] not in vol:
                l = l + 1
            
            while l < r and s[r] not in vol:
                r = r - 1
            
            s[l],s[r] = s[r],s[l]
            l = l + 1
            r = r - 1
        
        return "".join(s)