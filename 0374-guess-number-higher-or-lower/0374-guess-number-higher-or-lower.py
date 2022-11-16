class Solution:
    def guessNumber(self, n: int) -> int:
        
        l= 1
        r = n
        while l < r:
            m = (l + r) // 2
            if guess(m)==1:
                l = m + 1
            else:
                r = m
        
        return l