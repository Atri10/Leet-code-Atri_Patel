# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0

    
class Solution:
    def guessNumber(self, n: int) -> int:
        
        l= 1
        r = n
        
        while r>l:
            
            m = (l + r) // 2
            if guess(m)==1: l = m + 1
            else: r = m
        
        return l
                
        