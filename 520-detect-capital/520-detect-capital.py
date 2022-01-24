class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        t = word
        x = (word == t.upper())
        y = (word == t.lower())
        z = (word == t.title())
        
        return x or y or z